# --- 8. Productivity (71-80) ---
PRODUCTIVITY_APPS = [
    {
        "app_name": "Notion",
        "category": "Productivity",
        "one_liner": "Connected workspace for wiki, docs, and project management databases.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free account tier and self-serve integration token creation available.",
            "evidence_url": "https://www.notion.so/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.notion.com/reference",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://developers.notion.com/reference",
                "https://developers.notion.com/docs/authorization"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Airtable",
        "category": "Productivity",
        "one_liner": "Low-code platform for building collaborative spreadsheets and relational databases.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available with limits on base sizes self-serve.",
            "evidence_url": "https://www.airtable.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://airtable.com/developers/web/api/introduction",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://airtable.com/developers/web/api/introduction",
                "https://airtable.com/developers/web/api/oauth"
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
        "app_name": "Asana",
        "category": "Productivity",
        "one_liner": "Work management platform designed to help teams track and manage tasks.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free Personal plan available for up to 10 users.",
            "evidence_url": "https://asana.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.asana.com/reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://developers.asana.com/reference",
                "https://developers.asana.com/docs/oauth"
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
        "app_name": "Trello",
        "category": "Productivity",
        "one_liner": "Visual collaboration tool using cards and Kanban boards to manage projects.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for workspaces with up to 10 boards.",
            "evidence_url": "https://trello.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.atlassian.com/cloud/trello/rest/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.atlassian.com/cloud/trello/rest/",
                "https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/"
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
        "app_name": "ClickUp",
        "category": "Productivity",
        "one_liner": "All-in-one productivity platform for docs, goals, task management, and chat.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free Forever plan is available for personal use self-serve.",
            "evidence_url": "https://clickup.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://clickup.com/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://clickup.com/api/",
                "https://clickup.com/api/developer-portal/authentication/"
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
        "app_name": "Monday.com",
        "category": "Productivity",
        "one_liner": "Cloud work OS for task tracking, workflow design, and team collaboration.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free trial available on paid plans self-serve.",
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
        "app_name": "Todoist",
        "category": "Productivity",
        "one_liner": "To-do list and task manager app for tracking daily work tasks.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free plan available self-serve for personal task tracking.",
            "evidence_url": "https://todoist.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://developer.todoist.com/rest/v2/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://developer.todoist.com/rest/v2/",
                "https://developer.todoist.com/rest/v2/#authorization"
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
        "app_name": "Google Workspace",
        "category": "Productivity",
        "one_liner": "Suite of cloud computing, productivity, and collaboration tools by Google.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free trial available and API console access is self-serve via Google Cloud.",
            "evidence_url": "https://workspace.google.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.google.com/workspace",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "OAuth2 consent verification requirements and complex GCP credential provisioning.",
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://developers.google.com/workspace",
                "https://developers.google.com/workspace/guides/auth-overview"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 135,
            "agent_confidence": 0.93,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Dropbox",
        "category": "Productivity",
        "one_liner": "Cloud file hosting and cloud storage synchronization service.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free account signup available with 2GB storage and API access.",
            "evidence_url": "https://www.dropbox.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://www.dropbox.com/developers/documentation/http/documentation",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://www.dropbox.com/developers/documentation/http/documentation",
                "https://www.dropbox.com/developers/reference/oauth-guide"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 100,
            "agent_confidence": 0.97,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Box",
        "category": "Productivity",
        "one_liner": "Cloud content management and file sharing service for businesses.",
        "auth_methods": ["OAuth2", "JWT"],
        "self_serve": {
            "value": True,
            "reason": "Free developer account available for API testing.",
            "evidence_url": "https://developer.box.com/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.box.com/reference/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://developer.box.com/reference/",
                "https://developer.box.com/guides/authentication/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.95,
            "requires_human_review": False
        }
    }
]
