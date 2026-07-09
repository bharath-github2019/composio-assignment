# --- 9. Finance (81-90) ---
FINANCE_APPS = [
    {
        "app_name": "QuickBooks",
        "category": "Finance",
        "one_liner": "Accounting software package developed and marketed by Intuit for small businesses.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free sandbox account available via Intuit Developer Portal.",
            "evidence_url": "https://developer.intuit.com/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.intuit.com/app/developer/qbo/docs/api/resources/account",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "Complex multi-step OAuth2 configs, rigid validation checks, and sandbox data constraints.",
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developer.intuit.com/app/developer/qbo/docs/api/resources/account",
                "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Xero",
        "category": "Finance",
        "one_liner": "Cloud-based accounting software platform for small and medium-sized businesses.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free developer account and demo company available self-serve.",
            "evidence_url": "https://developer.xero.com/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.xero.com/documentation/api/accounting/overview",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.xero.com/documentation/api/accounting/overview",
                "https://developer.xero.com/documentation/guides/oauth2/overview"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Plaid",
        "category": "Finance",
        "one_liner": "Financial services platform connecting bank accounts to financial apps.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free developer account with 100 free bank link credentials.",
            "evidence_url": "https://plaid.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://plaid.com/docs/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://plaid.com/docs/api/",
                "https://plaid.com/docs/api/tokens/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.97,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Brex",
        "category": "Finance",
        "one_liner": "Financial technology platform offering corporate cards and expense management.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Developer keys can be generated in customer dashboard settings.",
            "evidence_url": "https://developer.brex.com/docs/quickstart/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.brex.com/openapi/webhooks_api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developer.brex.com/openapi/webhooks_api/",
                "https://developer.brex.com/docs/authentication/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Ramp",
        "category": "Finance",
        "one_liner": "Finance automation platform for corporate cards, expense management, and bill payments.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Developer portal allows instant API key generation for customer accounts.",
            "evidence_url": "https://docs.ramp.com/docs/getting-started"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.ramp.com/reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://docs.ramp.com/reference",
                "https://docs.ramp.com/docs/authentication"
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
        "app_name": "Bill.com",
        "category": "Finance",
        "one_liner": "Cloud-based software automating back-office financial operations for SMBs.",
        "auth_methods": ["API_Key", "Session"],
        "self_serve": {
            "value": False,
            "reason": "Developer sandbox account signup requires contacting developer support.",
            "evidence_url": "https://developer.bill.com/hc/en-us/articles/17399573887117-Developer-Sandbox-Account"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.bill.com/api-reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "Sandbox gating requires developer request review, and API uses unique session token generation.",
            "confidence_score": 0.88
        },
        "evidence": {
            "primary_docs": [
                "https://developer.bill.com/api-reference",
                "https://developer.bill.com/docs/getting-started"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 130,
            "agent_confidence": 0.88,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Gusto",
        "category": "Finance",
        "one_liner": "Cloud-based payroll, benefits, and human resource management software.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free developer account sandbox signup available.",
            "evidence_url": "https://docs.gusto.com/gh/docs/developer-sandbox"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.gusto.com/gh/reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://docs.gusto.com/gh/reference",
                "https://docs.gusto.com/gh/docs/oauth-introduction"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Wave",
        "category": "Finance",
        "one_liner": "Financial software provider for small businesses offering free bookkeeping.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free invoicing and accounting plans available self-serve.",
            "evidence_url": "https://www.waveapps.com/pricing"
        },
        "api_surface": {
            "type": "GraphQL",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.waveapps.com/hc/en-us/sections/360002821612-GraphQL-API",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://developer.waveapps.com/hc/en-us/sections/360002821612-GraphQL-API",
                "https://developer.waveapps.com/hc/en-us/articles/360020962652-Manage-API-Applications"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "FreshBooks",
        "category": "Finance",
        "one_liner": "Accounting software service designed for self-employed professionals and small businesses.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "30-day free trial available without credit card.",
            "evidence_url": "https://www.freshbooks.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://www.freshbooks.com/api/start",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://www.freshbooks.com/api/start",
                "https://www.freshbooks.com/api/authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 100,
            "agent_confidence": 0.93,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Expensify",
        "category": "Finance",
        "one_liner": "Software service automating receipt tracking and expense report management.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free trial and free card program available self-serve.",
            "evidence_url": "https://use.expensify.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://integrations.expensify.com/Integration-Server/doc/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://integrations.expensify.com/Integration-Server/doc/",
                "https://integrations.expensify.com/Integration-Server/doc/#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    }
]
