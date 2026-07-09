# --- 1. CRM (1-10) ---
CRM_APPS = [
    {
        "app_name": "Salesforce",
        "category": "CRM",
        "one_liner": "Enterprise customer relationship management platform for sales, service, and marketing.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": False,
            "reason": "Requires enterprise-tier paid license and contact sales for production API access.",
            "evidence_url": "https://www.salesforce.com/editions-pricing/sales-cloud/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.salesforce.com/docs",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "Complex OAuth2 setup, enterprise licensing gates, and SOAP/REST dual API complexity.",
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.salesforce.com/docs",
                "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_api.htm"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers/tree/main/src/salesforce"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 180,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "HubSpot",
        "category": "CRM",
        "one_liner": "Inbound marketing, sales, and customer service platform with developer-friendly APIs.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free developer accounts and sandbox environments are available self-serve.",
            "evidence_url": "https://developers.hubspot.com/docs/api/overview"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.hubspot.com/docs/api/overview",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://developers.hubspot.com/docs/api/overview",
                "https://developers.hubspot.com/docs/api/working-with-oauth"
            ],
            "secondary_sources": ["https://github.com/ComposioHQ/composio"],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Pipedrive",
        "category": "CRM",
        "one_liner": "Sales-focused CRM tool designed to help small businesses manage leads and deals.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available without entering a credit card.",
            "evidence_url": "https://www.pipedrive.com/en/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.pipedrive.com/docs/api/v1",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developers.pipedrive.com/docs/api/v1",
                "https://developers.pipedrive.com/docs/api/authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 95,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Zoho CRM",
        "category": "CRM",
        "one_liner": "Global customer relationship management platform for managing sales, marketing, and support.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free edition available for up to 3 users with basic features.",
            "evidence_url": "https://www.zoho.com/crm/comparison.html"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://www.zoho.com/crm/developer/docs/api/v3/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://www.zoho.com/crm/developer/docs/api/v3/",
                "https://www.zoho.com/crm/developer/docs/api/v3/oauth-overview.html"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 125,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Freshsales",
        "category": "CRM",
        "one_liner": "Sales CRM by Freshworks featuring AI-based lead scoring and built-in communication.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "21-day free trial available for self-serve signup.",
            "evidence_url": "https://www.freshworks.com/freshsales/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.freshsales.io/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://developer.freshsales.io/api/",
                "https://developer.freshsales.io/api/#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Close",
        "category": "CRM",
        "one_liner": "Inside sales CRM with built-in calling, SMS, and email automation features.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available for instant self-serve testing.",
            "evidence_url": "https://close.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.close.com/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developer.close.com/",
                "https://developer.close.com/#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 90,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Copper",
        "category": "CRM",
        "one_liner": "Productivity-first CRM built specifically for Google Workspace users and teams.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available on all tiers for self-serve setup.",
            "evidence_url": "https://www.copper.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.copper.com/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://developer.copper.com/",
                "https://developer.copper.com/sections/authentication/authentication.html"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Monday CRM",
        "category": "CRM",
        "one_liner": "Customizable sales CRM built on top of Monday.com work OS platform.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free trial and free basic tier available self-serve.",
            "evidence_url": "https://monday.com/pricing"
        },
        "api_surface": {
            "type": "GraphQL",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.monday.com/api-reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.monday.com/api-reference",
                "https://developer.monday.com/apps/docs/oauth"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 100,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Insightly",
        "category": "CRM",
        "one_liner": "CRM platform linking sales, project management, and marketing automation workflows.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 2 users, and free trials on paid tiers.",
            "evidence_url": "https://www.insightly.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://api.insightly.com/v3.1/Help",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://api.insightly.com/v3.1/Help",
                "https://api.insightly.com/v3.1/Help#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 95,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Agile CRM",
        "category": "CRM",
        "one_liner": "All-in-one CRM with sales, marketing, and service automation for SMBs.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 10 users with basic CRM features.",
            "evidence_url": "https://www.agilecrm.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://github.com/AgileCRM/rest-api",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.88
        },
        "evidence": {
            "primary_docs": [
                "https://github.com/AgileCRM/rest-api",
                "https://github.com/AgileCRM/rest-api#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.88,
            "requires_human_review": False
        }
    }
]
