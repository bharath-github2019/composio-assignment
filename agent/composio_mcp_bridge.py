from __future__ import annotations
import os, json, logging
from typing import Optional

logger = logging.getLogger(__name__)

COMPOSIO_API_KEY_ENV = "COMPOSIO_API_KEY"
MOCK_MODE_FLAG = "COMPOSIO_MOCK_MODE"


class ComposioMCPBridge:
    """
    Bridges the research pipeline with Composio's MCP (Model Context Protocol)
    server for live tool execution and managed authentication.

    Two modes:
      - PRODUCTION (default when COMPOSIO_API_KEY is set and COMPOSIO_MOCK_MODE != 1):
        Uses Composio SDK + MCP to execute real API calls against each app's docs,
        fetch auth schemas, and validate endpoint surfaces.

      - MOCK (fallback when COMPOSIO_API_KEY is missing or COMPOSIO_MOCK_MODE=1):
        Returns structurally valid mock data matching the Pydantic schema.
        Every mock record is flagged with "confidence_source": "simulated".
    """

    def __init__(self):
        self.api_key = os.environ.get(COMPOSIO_API_KEY_ENV)
        self.mock_mode = (
            self.api_key is None
            or os.environ.get(MOCK_MODE_FLAG, "0") == "1"
        )
        self._client = None
        self._mcp_session = None

        if not self.mock_mode:
            self._init_production()
        else:
            logger.info("ComposioMCPBridge: MOCK mode (no API key or mock flag set)")

    # ------------------------------------------------------------------
    # Production initialisation
    # ------------------------------------------------------------------
    def _init_production(self):
        try:
            from composio_mcp import ComposioClient  # type: ignore[import-untyped]
            self._client = ComposioClient(api_key=self.api_key)
            self._mcp_session = self._client.create_session()
            logger.info("ComposioMCPBridge: PRODUCTION mode — connected to Composio MCP")
        except ImportError:
            logger.warning(
                "composio-mcp package not installed. Falling back to MOCK mode. "
                "Run: pip install composio-mcp"
            )
            self.mock_mode = True
        except Exception as exc:
            logger.error("ComposioMCPBridge: failed to init production client: %s", exc)
            self.mock_mode = True

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------
    @property
    def is_mock(self) -> bool:
        return self.mock_mode

    @property
    def client(self):
        return self._client

    @property
    def mcp_session(self):
        return self._mcp_session

    # ------------------------------------------------------------------
    # Research actions
    # ------------------------------------------------------------------
    def fetch_auth_schema(self, app_name: str, docs_url: str) -> dict:
        """
        Return the authentication schema for *app_name*.

        Production: queries the Composio tool registry for the app's
        auth configuration (OAuth2 scopes, API key format, etc.).

        Mock: returns a placeholder with a note that live data was
        not fetched.
        """
        if self.mock_mode:
            return {
                "app_name": app_name,
                "source": docs_url,
                "auth_methods": ["API_Key", "OAuth2"],
                "confidence_source": "simulated",
                "note": "Mock response — set COMPOSIO_API_KEY for live data",
            }

        try:
            schema = self._mcp_session.get_tool_auth_schema(app_name)
            return {
                "app_name": app_name,
                "source": docs_url,
                "auth_methods": schema.get("auth_methods", []),
                "confidence_source": "composio_mcp",
            }
        except Exception as exc:
            logger.error("MCP auth fetch failed for %s: %s", app_name, exc)
            return {"app_name": app_name, "error": str(exc)}

    def verify_endpoint(self, app_name: str, endpoint: str) -> dict:
        """
        Probe a single API endpoint to confirm it responds (production) or
        return a mock confirmation (mock mode).
        """
        if self.mock_mode:
            return {
                "app_name": app_name,
                "endpoint": endpoint,
                "reachable": True,
                "confidence_source": "simulated",
            }

        try:
            result = self._mcp_session.execute_tool(
                tool_name=f"{app_name}_api",
                parameters={"endpoint": endpoint, "method": "GET"},
            )
            return {
                "app_name": app_name,
                "endpoint": endpoint,
                "reachable": result.get("status", 0) < 500,
                "status_code": result.get("status"),
                "confidence_source": "composio_mcp",
            }
        except Exception as exc:
            logger.error("Endpoint verification failed for %s%s: %s", app_name, endpoint, exc)
            return {"app_name": app_name, "endpoint": endpoint, "reachable": False, "error": str(exc)}

    def batch_fetch_auth_schemas(self, apps: list[dict]) -> list[dict]:
        """Convenience: fetch auth schemas for a list of app dicts."""
        return [self.fetch_auth_schema(a["app_name"], a.get("evidence", {}).get("primary_docs", [""])[0]) for a in apps]

    # ------------------------------------------------------------------
    # Health
    # ------------------------------------------------------------------
    def health(self) -> dict:
        return {
            "mode": "mock" if self.mock_mode else "production",
            "api_key_set": self.api_key is not None,
            "client_connected": self._client is not None,
            "mcp_session_active": self._mcp_session is not None,
        }


# ------------------------------------------------------------------
# Singleton shortcut
# ------------------------------------------------------------------
_bridge: Optional[ComposioMCPBridge] = None


def get_bridge() -> ComposioMCPBridge:
    global _bridge
    if _bridge is None:
        _bridge = ComposioMCPBridge()
    return _bridge
