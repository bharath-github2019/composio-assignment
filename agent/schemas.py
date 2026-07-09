"""
Composio Research Agent - Pydantic Schemas
Strict validation for all 100 app research extractions.
Schema version aligned with Section 3 of the Research Brief.
"""

from __future__ import annotations
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, Literal
from datetime import datetime
from enum import Enum


# --- Enums ---

class CategoryEnum(str, Enum):
    CRM = "CRM"
    SUPPORT = "Support"
    MESSAGING = "Messaging"
    MARKETING = "Marketing"
    ECOMMERCE = "Ecommerce"
    DATA_SEO = "Data/SEO"
    DEVTOOLS = "DevTools"
    PRODUCTIVITY = "Productivity"
    FINANCE = "Finance"
    AI_MEDIA = "AI/Media"


class AuthMethod(str, Enum):
    OAUTH2 = "OAuth2"
    API_KEY = "API_Key"
    BASIC_AUTH = "Basic_Auth"
    JWT = "JWT"
    SESSION = "Session"
    MTLS = "mTLS"
    OTHER = "Other"


class APIType(str, Enum):
    REST = "REST"
    GRAPHQL = "GraphQL"
    GRPC = "gRPC"
    WEBSOCKET = "WebSocket"
    NONE = "None"


class APIBreadth(str, Enum):
    NARROW = "Narrow (<10 endpoints)"
    MEDIUM = "Medium (10-50)"
    BROAD = "Broad (>50)"


class BuildabilityVerdict(str, Enum):
    READY = "Ready"
    NEEDS_WORK = "Needs_Work"
    BLOCKED = "Blocked"


# --- Sub-models ---

class SelfServe(BaseModel):
    """Self-serve access assessment."""
    value: bool = Field(..., description="True if free tier/trial exists AND no sales contact required")
    reason: str = Field(..., description="Explanation, e.g. 'free tier available', 'requires contact sales'")
    evidence_url: str = Field(..., description="URL to pricing or signup page as evidence")


class APISurface(BaseModel):
    """API surface characterization."""
    type: APIType = Field(..., description="Primary API protocol type")
    breadth: APIBreadth = Field(..., description="Endpoint count estimate")
    docs_url: str = Field(..., description="Primary API documentation URL")
    mcp_exists: bool = Field(..., description="Whether an MCP server or agent toolkit exists for this app")


class Buildability(BaseModel):
    """Integration buildability assessment."""
    verdict: BuildabilityVerdict = Field(..., description="Ready / Needs_Work / Blocked")
    primary_blocker: Optional[str] = Field(
        None, 
        description="Primary blocker description (only if verdict is not Ready)"
    )
    confidence_score: float = Field(
        ..., 
        ge=0.0, le=1.0,
        description="Confidence in verdict. 1.0=official docs explicit, 0.8-0.9=inferred, 0.6-0.7=community, <0.6=conflicting"
    )

    @field_validator('primary_blocker', mode='before')
    @classmethod
    def clean_primary_blocker(cls, v):
        if isinstance(v, str):
            clean_val = v.strip().lower()
            if clean_val in ('none', 'null', 'n/a', ''):
                return None
        return v

    @model_validator(mode='after')
    def validate_blocker_consistency(self):
        if self.verdict == BuildabilityVerdict.READY and self.primary_blocker is not None:
            raise ValueError("primary_blocker must be None when verdict is 'Ready'")
        if self.verdict != BuildabilityVerdict.READY and not self.primary_blocker:
            raise ValueError("primary_blocker is required when verdict is not 'Ready'")
        return self


class Evidence(BaseModel):
    """Evidence and source tracking."""
    primary_docs: list[str] = Field(..., min_length=1, description="Primary documentation URLs")
    secondary_sources: list[str] = Field(default_factory=list, description="Secondary/community source URLs")
    extraction_timestamp: str = Field(..., description="ISO 8601 timestamp of extraction")

    @field_validator('extraction_timestamp')
    @classmethod
    def validate_timestamp(cls, v):
        try:
            datetime.fromisoformat(v.replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            raise ValueError(f"Invalid ISO 8601 timestamp: {v}")
        return v


class Metadata(BaseModel):
    """Research metadata and quality tracking."""
    research_time_seconds: int = Field(..., ge=0, description="Time spent researching this app in seconds")
    agent_confidence: float = Field(
        ..., 
        ge=0.0, le=1.0,
        description="Overall agent confidence in the extraction"
    )
    requires_human_review: bool = Field(
        ..., 
        description="True if any field has confidence < 0.7"
    )


# --- Main Schema ---

class AppResearch(BaseModel):
    """
    Complete research extraction for a single application.
    Matches Section 3 of the Composio Research Brief exactly.
    """
    app_name: str = Field(..., min_length=1, description="Application name")
    category: CategoryEnum = Field(..., description="Application category")
    one_liner: str = Field(..., description="Core function description (≤15 words)")
    auth_methods: list[AuthMethod] = Field(..., min_length=1, description="Supported authentication methods")
    self_serve: SelfServe
    api_surface: APISurface
    buildability: Buildability
    evidence: Evidence
    metadata: Metadata

    @field_validator('one_liner')
    @classmethod
    def validate_one_liner_length(cls, v):
        word_count = len(v.split())
        if word_count > 15:
            raise ValueError(f"one_liner must be ≤15 words, got {word_count}")
        return v

    @model_validator(mode='after')
    def validate_human_review_flag(self):
        """Auto-flag for human review if confidence is low."""
        if self.buildability.confidence_score < 0.7 and not self.metadata.requires_human_review:
            raise ValueError(
                "requires_human_review must be True when confidence_score < 0.7"
            )
        return self


class ResearchDataset(BaseModel):
    """Complete dataset of all app research results."""
    schema_version: str = Field(default="1.0")
    total_apps: int = Field(..., ge=1)
    extraction_start: str = Field(..., description="ISO 8601 timestamp of pipeline start")
    extraction_end: Optional[str] = Field(None, description="ISO 8601 timestamp of pipeline end")
    results: list[AppResearch] = Field(default_factory=list)

    @model_validator(mode='after')
    def validate_count(self):
        if len(self.results) != self.total_apps:
            raise ValueError(
                f"total_apps ({self.total_apps}) doesn't match results count ({len(self.results)})"
            )
        return self


# --- Validation Utilities ---

class SchemaValidationReport(BaseModel):
    """Report from schema validation run."""
    timestamp: str
    apps_tested: list[str]
    apps_passed: list[str]
    apps_failed: list[str]
    errors: dict = Field(default_factory=dict, description="app_name -> list of error messages")
    schema_version: str = "1.0"
    status: Literal["VALIDATED", "FAILED"]


def validate_app_json(data: dict) -> tuple[bool, list[str]]:
    """
    Validate a single app's JSON against the schema.
    Returns (is_valid, list_of_errors).
    """
    errors = []
    try:
        AppResearch(**data)
        return True, []
    except Exception as e:
        error_str = str(e)
        errors.append(error_str)
        return False, errors


def validate_dataset(data: dict) -> tuple[bool, list[str]]:
    """
    Validate the complete research dataset.
    Returns (is_valid, list_of_errors).
    """
    errors = []
    try:
        ResearchDataset(**data)
        return True, []
    except Exception as e:
        errors.append(str(e))
        return False, errors


if __name__ == "__main__":
    # Quick self-test with a minimal valid example
    import json

    test_app = {
        "app_name": "TestApp",
        "category": "DevTools",
        "one_liner": "A test application for schema validation",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available",
            "evidence_url": "https://example.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://example.com/docs",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": ["https://example.com/docs/api"],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T16:53:00+05:30"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    }

    is_valid, errors = validate_app_json(test_app)
    if is_valid:
        print("✅ SCHEMA SELF-TEST PASSED")
        print(json.dumps(test_app, indent=2))
    else:
        print("❌ SCHEMA SELF-TEST FAILED")
        for e in errors:
            print(f"  ERROR: {e}")
