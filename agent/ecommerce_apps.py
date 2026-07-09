# --- 5. Ecommerce (41-50) ---
ECOMMERCE_APPS = [
    {
        "app_name": "Shopify",
        "category": "Ecommerce",
        "one_liner": "E-commerce platform for online stores and retail point-of-sale systems.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free trial available and free partner account to build developer apps.",
            "evidence_url": "https://www.shopify.com/pricing"
        },
        "api_surface": {
            "type": "GraphQL",
            "breadth": "Broad (>50)",
            "docs_url": "https://shopify.dev/docs/api/admin-graphql",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://shopify.dev/docs/api/admin-graphql",
                "https://shopify.dev/docs/apps/auth"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 125,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Stripe",
        "category": "Ecommerce",
        "one_liner": "Payment processing platform for internet businesses with comprehensive financial APIs.",
        "auth_methods": ["API_Key", "OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free account signup with no sales contact required. Pay-as-you-go pricing.",
            "evidence_url": "https://stripe.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.stripe.com/api",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 1.0
        },
        "evidence": {
            "primary_docs": [
                "https://docs.stripe.com/api",
                "https://docs.stripe.com/api/authentication"
            ],
            "secondary_sources": [
                "https://github.com/stripe/ai"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 1.0,
            "requires_human_review": False
        }
    },
    {
        "app_name": "WooCommerce",
        "category": "Ecommerce",
        "one_liner": "Open-source e-commerce plugin for WordPress websites.",
        "auth_methods": ["OAuth2", "API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Completely free open-source plugin requiring no sales contact or license fees.",
            "evidence_url": "https://woocommerce.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://woocommerce.github.io/woocommerce-rest-api-docs/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://woocommerce.github.io/woocommerce-rest-api-docs/",
                "https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 100,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "BigCommerce",
        "category": "Ecommerce",
        "one_liner": "SaaS e-commerce platform offering online store creation, SEO, and marketing.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "15-day free trial available self-serve.",
            "evidence_url": "https://www.bigcommerce.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.bigcommerce.com/docs/rest-content",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developer.bigcommerce.com/docs/rest-content",
                "https://developer.bigcommerce.com/docs/start/authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Square",
        "category": "Ecommerce",
        "one_liner": "Financial services, merchant services, and mobile payment platform.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free developer account and testing sandbox available instantly.",
            "evidence_url": "https://squareup.com/us/en/developers"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.squareup.com/reference/square",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://developer.squareup.com/reference/square",
                "https://developer.squareup.com/docs/oauth-api/overview"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.97,
            "requires_human_review": False
        }
    },
    {
        "app_name": "PayPal",
        "category": "Ecommerce",
        "one_liner": "Global online payment system supporting online money transfers.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free developer account and API credential creation via PayPal Developer Portal.",
            "evidence_url": "https://developer.paypal.com/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.paypal.com/api/rest/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://developer.paypal.com/api/rest/",
                "https://developer.paypal.com/api/rest/authentication/"
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
        "app_name": "Magento",
        "category": "Ecommerce",
        "one_liner": "Open-source e-commerce platform written in PHP by Adobe.",
        "auth_methods": ["OAuth2", "API_Key", "JWT"],
        "self_serve": {
            "value": True,
            "reason": "Open Source edition is free to download and build on self-serve.",
            "evidence_url": "https://business.adobe.com/products/magento/magento-open-source.html"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.adobe.com/commerce/web-api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://developer.adobe.com/commerce/web-api/",
                "https://developer.adobe.com/commerce/web-api/rest/authentication/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 130,
            "agent_confidence": 0.93,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Chargebee",
        "category": "Ecommerce",
        "one_liner": "Subscription billing and revenue management platform for SaaS businesses.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free trial tier and developer sandbox environment available.",
            "evidence_url": "https://www.chargebee.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://apidocs.chargebee.com/list/api/v2",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://apidocs.chargebee.com/list/api/v2",
                "https://apidocs.chargebee.com/list/api/v2#authentication"
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
        "app_name": "Recurly",
        "category": "Ecommerce",
        "one_liner": "Subscription billing platform for businesses to manage billing and recurring payments.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free sandbox account available for developer testing.",
            "evidence_url": "https://recurly.com/developers/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.recurly.com/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developers.recurly.com/api/",
                "https://developers.recurly.com/api/#section/Authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Adyen",
        "category": "Ecommerce",
        "one_liner": "Global multichannel payment company providing unified checkout workflows.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free test account available self-serve for developer integration.",
            "evidence_url": "https://www.adyen.com/signup"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.adyen.com/api-explorer/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://docs.adyen.com/api-explorer/",
                "https://docs.adyen.com/development-resources/api-credentials"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    }
]
