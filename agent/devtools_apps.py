# --- 7. DevTools (61-70) ---
DEVTOOLS_APPS = [
    {
        "app_name": "GitHub",
        "category": "DevTools",
        "one_liner": "Developer platform for code hosting, version control, and collaboration.",
        "auth_methods": ["OAuth2", "API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free account registration and API access via Personal Access Tokens.",
            "evidence_url": "https://github.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.github.com/en/rest",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 1.0
        },
        "evidence": {
            "primary_docs": [
                "https://docs.github.com/en/rest",
                "https://docs.github.com/en/graphql"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers/tree/main/src/github"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 1.0,
            "requires_human_review": False
        }
    },
    {
        "app_name": "GitLab",
        "category": "DevTools",
        "one_liner": "DevOps lifecycle tool providing wiki, issue-tracking, and CI/CD pipeline features.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free SaaS tier and self-hosted Open Source editions available.",
            "evidence_url": "https://about.gitlab.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.gitlab.com/ee/api/rest/",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://docs.gitlab.com/ee/api/rest/",
                "https://docs.gitlab.com/ee/api/graphql/"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Bitbucket",
        "category": "DevTools",
        "one_liner": "Git repository management solution designed for professional teams by Atlassian.",
        "auth_methods": ["OAuth2", "API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 5 users self-serve.",
            "evidence_url": "https://bitbucket.org/product/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.atlassian.com/cloud/bitbucket/rest/intro/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.atlassian.com/cloud/bitbucket/rest/intro/",
                "https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/"
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
        "app_name": "Jira",
        "category": "DevTools",
        "one_liner": "Issue tracking and agile project management software for software developers.",
        "auth_methods": ["OAuth2", "API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 10 users self-serve.",
            "evidence_url": "https://www.atlassian.com/software/jira/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/",
                "https://developer.atlassian.com/cloud/jira/platform/jira-rest-api-oauth-2-0-authorization-code-grants-3lo/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.97,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Linear",
        "category": "DevTools",
        "one_liner": "Issue tracker for software developer teams with modern keyboard shortcuts.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free plan available for unlimited users with basic usage caps.",
            "evidence_url": "https://linear.app/pricing"
        },
        "api_surface": {
            "type": "GraphQL",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.linear.app/docs/graphql/overview",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://developers.linear.app/docs/graphql/overview",
                "https://developers.linear.app/docs/oauth/overview"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 95,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "CircleCI",
        "category": "DevTools",
        "one_liner": "Continuous integration and delivery platform automating software builds.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free plan includes 6,000 build minutes per month.",
            "evidence_url": "https://circleci.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://circleci.com/docs/api/v2/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://circleci.com/docs/api/v2/",
                "https://circleci.com/docs/api/v2/#section/Authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 90,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Datadog",
        "category": "DevTools",
        "one_liner": "Observability and security monitoring service for cloud-scale applications.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "14-day free trial available self-serve.",
            "evidence_url": "https://www.datadoghq.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.datadoghq.com/api/latest/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://docs.datadoghq.com/api/latest/",
                "https://docs.datadoghq.com/api/latest/authentication/"
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
        "app_name": "PagerDuty",
        "category": "DevTools",
        "one_liner": "Incident response platform for enterprise IT monitoring and operations alerts.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 5 users, and 14-day trial.",
            "evidence_url": "https://www.pagerduty.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.pagerduty.com/api-reference/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.pagerduty.com/api-reference/",
                "https://developer.pagerduty.com/docs/ZG9jOjI3NDkwMDM-oauth-2-0"
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
        "app_name": "Sentry",
        "category": "DevTools",
        "one_liner": "Open-source application monitoring platform for real-time error tracking and performance.",
        "auth_methods": ["API_Key", "OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free Developer plan available with basic event volume quotas.",
            "evidence_url": "https://sentry.io/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.sentry.io/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://docs.sentry.io/api/",
                "https://docs.sentry.io/api/auth/"
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
        "app_name": "Postman",
        "category": "DevTools",
        "one_liner": "API platform for building, testing, and managing developer APIs.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 3 users self-serve.",
            "evidence_url": "https://www.postman.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://www.postman.com/postman/workspace/postman-public-workspace/documentation/1295954-c918c50e-b8d2-436f-a6ab-6b71887e59b5",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://www.postman.com/postman/workspace/postman-public-workspace/documentation/1295954-c918c50e-b8d2-436f-a6ab-6b71887e59b5"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    }
]
