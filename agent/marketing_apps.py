# --- 4. Marketing (31-40) ---
MARKETING_APPS = [
    {
        "app_name": "Mailchimp",
        "category": "Marketing",
        "one_liner": "All-in-one email marketing and audience management automation platform.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free marketing plan available self-serve.",
            "evidence_url": "https://mailchimp.com/pricing/marketing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://mailchimp.com/developer/marketing/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://mailchimp.com/developer/marketing/api/",
                "https://mailchimp.com/developer/marketing/docs/fundamentals/#authenticate-with-an-api-key"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "HubSpot Marketing",
        "category": "Marketing",
        "one_liner": "Marketing automation software for attracting visitors and closing deals.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free account sign up and free tools available self-serve.",
            "evidence_url": "https://www.hubspot.com/pricing/marketing"
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
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://developers.hubspot.com/docs/api/overview",
                "https://developers.hubspot.com/docs/api/working-with-oauth"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Marketo",
        "category": "Marketing",
        "one_liner": "Enterprise marketing automation software by Adobe for lead management and engagement.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": False,
            "reason": "No self-serve signup or pricing available. Enterprise sales contract required.",
            "evidence_url": "https://business.adobe.com/products/marketo/pricing.html"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.marketo.com/rest-api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Blocked",
            "primary_blocker": "Developer access is tied strictly to active paid enterprise instances.",
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://developers.marketo.com/rest-api/",
                "https://developers.marketo.com/rest-api/authentication/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 140,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "ActiveCampaign",
        "category": "Marketing",
        "one_liner": "Customer experience automation platform combining email marketing and CRM.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available for self-serve onboarding.",
            "evidence_url": "https://www.activecampaign.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.activecampaign.com/reference/overview",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developers.activecampaign.com/reference/overview",
                "https://developers.activecampaign.com/reference/authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 100,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Brevo",
        "category": "Marketing",
        "one_liner": "Marketing platform offering email, SMS, and chat automation for SMBs.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free plan available for up to 300 emails/day self-serve.",
            "evidence_url": "https://www.brevo.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.brevo.com/reference/how-to-authenticate-your-api-request",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developers.brevo.com/reference/how-to-authenticate-your-api-request"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 90,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Klaviyo",
        "category": "Marketing",
        "one_liner": "Marketing automation platform specializing in e-commerce email and SMS.",
        "auth_methods": ["API_Key", "OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free account sign up available with full developer API access.",
            "evidence_url": "https://www.klaviyo.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.klaviyo.com/en/reference/api_overview",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://developers.klaviyo.com/en/reference/api_overview",
                "https://developers.klaviyo.com/en/docs/authenticate_your_api_requests"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "ConvertKit",
        "category": "Marketing",
        "one_liner": "Creator marketing platform offering email newsletters and landing pages.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 10k subscribers.",
            "evidence_url": "https://convertkit.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://developers.convertkit.com/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://developers.convertkit.com/",
                "https://developers.convertkit.com/#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 95,
            "agent_confidence": 0.93,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Constant Contact",
        "category": "Marketing",
        "one_liner": "Online marketing tool providing email campaigns, website builder, and social tools.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "60-day free trial available for self-serve signup.",
            "evidence_url": "https://www.constantcontact.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.constantcontact.com/api_reference/index.html",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://developer.constantcontact.com/api_reference/index.html",
                "https://developer.constantcontact.com/api_guide/oauth2_overview.html"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Drip",
        "category": "Marketing",
        "one_liner": "Marketing automation engine for e-commerce brands offering email and SMS workflows.",
        "auth_methods": ["API_Key", "OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available on all tiers self-serve.",
            "evidence_url": "https://www.drip.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.drip.com/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developer.drip.com/",
                "https://developer.drip.com/#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 100,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Customer.io",
        "category": "Marketing",
        "one_liner": "Automated messaging platform for sending newsletters, push notifications, and emails.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available self-serve.",
            "evidence_url": "https://customer.io/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://customer.io/docs/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://customer.io/docs/api/",
                "https://customer.io/docs/api/#section/Authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.93,
            "requires_human_review": False
        }
    }
]
