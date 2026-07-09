# --- 6. Data/SEO (51-60) ---
DATA_SEO_APPS = [
    {
        "app_name": "Ahrefs",
        "category": "Data/SEO",
        "one_liner": "SEO toolset for link building, keyword research, and competitor analysis.",
        "auth_methods": ["API_Key", "OAuth2"],
        "self_serve": {
            "value": False,
            "reason": "API access requires enterprise subscription and custom pricing contract.",
            "evidence_url": "https://ahrefs.com/api/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://ahrefs.com/api/documentation",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "High price gate and manual enterprise contract requirements for API developer tokens.",
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://ahrefs.com/api/documentation",
                "https://ahrefs.com/api/documentation/authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 130,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "SEMrush",
        "category": "Data/SEO",
        "one_liner": "SEO, PPC, and content marketing platform offering detailed analytics.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": False,
            "reason": "API only available on expensive Business plan subscription ($499/mo).",
            "evidence_url": "https://www.semrush.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://www.semrush.com/api/documentation/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "High tier gating where API access is restricted to expensive Business plans.",
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://www.semrush.com/api/documentation/",
                "https://www.semrush.com/kb/897-api-units"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 125,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Moz",
        "category": "Data/SEO",
        "one_liner": "SEO software for search engine optimization tracking and domain metrics.",
        "auth_methods": ["Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier Mozscape API access available self-serve.",
            "evidence_url": "https://moz.com/help/moz-api/mozscape/getting-started-with-mozscape"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://moz.com/help/moz-api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://moz.com/help/moz-api/",
                "https://moz.com/help/moz-api/mozscape/api-reference"
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
        "app_name": "Google Analytics",
        "category": "Data/SEO",
        "one_liner": "Web analytics service by Google tracking and reporting website traffic.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free account registration and API developer access via Google Cloud Console.",
            "evidence_url": "https://marketingplatform.google.com/about/analytics/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.google.com/analytics",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://developers.google.com/analytics",
                "https://developers.google.com/analytics/devguides/reporting/data/v1"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.97,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Mixpanel",
        "category": "Data/SEO",
        "one_liner": "Product analytics service tracking user interactions with web and mobile applications.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 100,000 monthly tracked users.",
            "evidence_url": "https://mixpanel.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.mixpanel.com/reference/api-reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://developer.mixpanel.com/reference/api-reference",
                "https://developer.mixpanel.com/reference/service-accounts"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Amplitude",
        "category": "Data/SEO",
        "one_liner": "Product analytics platform helping teams track user behavior and run digital experiments.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free Starter plan offers up to 10 million events per month.",
            "evidence_url": "https://amplitude.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://www.docs.developers.amplitude.com/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://www.docs.developers.amplitude.com/",
                "https://www.docs.developers.amplitude.com/analytics/apis/export-api/"
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
        "app_name": "Segment",
        "category": "Data/SEO",
        "one_liner": "Customer data platform collecting, cleaning, and routing customer event data.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 1,000 monthly visitors.",
            "evidence_url": "https://segment.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://segment.com/docs/api/public-api/",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://segment.com/docs/api/public-api/",
                "https://segment.com/docs/api/public-api/reference/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Clearbit",
        "category": "Data/SEO",
        "one_liner": "B2B marketing intelligence platform for data enrichment and lead generation.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available with credit limitations self-serve.",
            "evidence_url": "https://clearbit.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://dashboard.clearbit.com/docs",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://dashboard.clearbit.com/docs",
                "https://dashboard.clearbit.com/docs#enrichment-api"
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
        "app_name": "PitchBook",
        "category": "Data/SEO",
        "one_liner": "Financial data platform for private and public capital markets intelligence.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": False,
            "reason": "API access requires enterprise contract, subscription, and custom credit billing.",
            "evidence_url": "https://pitchbook.com/data/direct-data"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://pitchbook.com/data/direct-data",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "No self-serve access, proprietary sales-gated API provisioning, and gated endpoints.",
            "confidence_score": 0.85
        },
        "evidence": {
            "primary_docs": [
                "https://pitchbook.com/data/direct-data",
                "https://api.pitchbook.com"
            ],
            "secondary_sources": [
                "https://dlthub.com/docs/dlt-ecosystem/verified-sources/pitchbook"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 130,
            "agent_confidence": 0.85,
            "requires_human_review": True
        }
    },
    {
        "app_name": "Crunchbase",
        "category": "Data/SEO",
        "one_liner": "Platform finding business information about private and public companies.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": False,
            "reason": "API access is gated under paid Crunchbase Enterprise subscription.",
            "evidence_url": "https://data.crunchbase.com/docs/pricing-packages"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://data.crunchbase.com/docs",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "Requires Crunchbase Enterprise license for developer API access key.",
            "confidence_score": 0.9
        },
        "evidence": {
            "primary_docs": [
                "https://data.crunchbase.com/docs",
                "https://data.crunchbase.com/docs/using-the-api"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 125,
            "agent_confidence": 0.9,
            "requires_human_review": False
        }
    }
]
