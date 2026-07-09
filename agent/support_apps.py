# --- 2. Support (11-20) ---
SUPPORT_APPS = [
    {
        "app_name": "Zendesk",
        "category": "Support",
        "one_liner": "Customer service software and support ticket management platform.",
        "auth_methods": ["OAuth2", "API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available on Suite Team/Growth tiers self-serve.",
            "evidence_url": "https://www.zendesk.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.zendesk.com/api-reference/",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://developer.zendesk.com/api-reference/",
                "https://developer.zendesk.com/api-reference/ticketing/introduction/"
            ],
            "secondary_sources": ["https://github.com/modelcontextprotocol/servers"],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Intercom",
        "category": "Support",
        "one_liner": "Customer messaging and live chat platform for sales, marketing, and support.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available self-serve.",
            "evidence_url": "https://www.intercom.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.intercom.com/building-apps/docs",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developers.intercom.com/building-apps/docs",
                "https://developers.intercom.com/intercom-api-reference/reference/welcome"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Freshdesk",
        "category": "Support",
        "one_liner": "Cloud-based customer service software and helpdesk ticket tracking system.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 10 agents, free trial on paid plans.",
            "evidence_url": "https://freshdesk.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.freshdesk.com/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://developers.freshdesk.com/api/",
                "https://developers.freshdesk.com/api/#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 95,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "ServiceNow",
        "category": "Support",
        "one_liner": "Enterprise cloud platform for digital workflows and IT service management.",
        "auth_methods": ["OAuth2", "Basic_Auth"],
        "self_serve": {
            "value": False,
            "reason": "Enterprise licensing required; developer sandbox available but production API requires sales contract.",
            "evidence_url": "https://www.servicenow.com/pricing.html"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.servicenow.com/",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "Complex enterprise security policies, mTLS requirements, and gated production pricing.",
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://developer.servicenow.com/",
                "https://docs.servicenow.com/bundle/washingtondc-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 150,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Jira Service Management",
        "category": "Support",
        "one_liner": "IT service desk and customer support portal by Atlassian.",
        "auth_methods": ["OAuth2", "API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 3 agents, and 7-day trials for higher plans.",
            "evidence_url": "https://www.atlassian.com/software/jira/service-management/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/",
                "https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-request/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 130,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Help Scout",
        "category": "Support",
        "one_liner": "Shared inbox and customer support tool designed for growing teams.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "15-day free trial available on Standard and Plus plans.",
            "evidence_url": "https://www.helpscout.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.helpscout.com/mailbox-api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://developer.helpscout.com/mailbox-api/",
                "https://developer.helpscout.com/mailbox-api/endpoints/conversations/create/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Kayako",
        "category": "Support",
        "one_liner": "Help desk and customer journey tracking platform.",
        "auth_methods": ["OAuth2", "API_Key", "Basic_Auth"],
        "self_serve": {
            "value": False,
            "reason": "Requires contacting sales for demo and price plans; no self-serve free trial or signup.",
            "evidence_url": "https://www.kayako.com/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.kayako.com/api/v1/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Blocked",
            "primary_blocker": "API is gated behind manual sales contact and enterprise subscription contract.",
            "confidence_score": 0.88
        },
        "evidence": {
            "primary_docs": [
                "https://developer.kayako.com/api/v1/",
                "https://developer.kayako.com/api/v1/reference/conversations/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 125,
            "agent_confidence": 0.88,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Zoho Desk",
        "category": "Support",
        "one_liner": "Context-aware customer service help desk software.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 3 agents, and 15-day trial.",
            "evidence_url": "https://www.zoho.com/desk/pricing.html"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://desk.zoho.com/support/APIDocument.do",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://desk.zoho.com/support/APIDocument.do",
                "https://desk.zoho.com/support/APIDocument.do#Authentication"
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
        "app_name": "Front",
        "category": "Support",
        "one_liner": "Collaborative inbox combining email, chat, and sms channels into one workspace.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "7-day free trial available for self-serve sign up.",
            "evidence_url": "https://front.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://dev.frontapp.com/reference/welcome",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://dev.frontapp.com/reference/welcome",
                "https://dev.frontapp.com/docs/oauth"
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
        "app_name": "Gladly",
        "category": "Support",
        "one_liner": "People-centered customer service platform that focuses on lifelong relationships.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": False,
            "reason": "No self-serve signup or free trial. Enterprise-only platform requiring sales contact.",
            "evidence_url": "https://www.gladly.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://connect.gladly.com/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Blocked",
            "primary_blocker": "Requires enterprise custom onboarding and sales-gated API provisioning.",
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://connect.gladly.com/api/",
                "https://connect.gladly.com/api/reference/v1/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 135,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    }
]
