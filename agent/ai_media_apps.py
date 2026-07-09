# --- 10. AI/Media (91-100) ---
AI_MEDIA_APPS = [
    {
        "app_name": "OpenAI",
        "category": "AI/Media",
        "one_liner": "Artificial intelligence research laboratory developer of GPT models.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Developer accounts are self-serve with pay-as-you-go credit card billing.",
            "evidence_url": "https://openai.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://platform.openai.com/docs/api-reference",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://platform.openai.com/docs/api-reference",
                "https://platform.openai.com/docs/api-reference/authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 105,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Anthropic",
        "category": "AI/Media",
        "one_liner": "AI safety and research company developer of Claude language models.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Anthropic Console allows self-serve signup and credit purchases.",
            "evidence_url": "https://www.anthropic.com/api"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://docs.anthropic.com/en/api/getting-started",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://docs.anthropic.com/en/api/getting-started",
                "https://docs.anthropic.com/en/api/messages"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Cohere",
        "category": "AI/Media",
        "one_liner": "AI platform providing enterprise natural language processing models.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free trial key available self-serve for development usage.",
            "evidence_url": "https://cohere.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.cohere.com/reference/about",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://docs.cohere.com/reference/about",
                "https://docs.cohere.com/reference/auth"
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
        "app_name": "ElevenLabs",
        "category": "AI/Media",
        "one_liner": "Voice technology research company offering realistic text-to-speech voice generation.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free plan includes 10,000 characters per month.",
            "evidence_url": "https://elevenlabs.io/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://elevenlabs.io/docs/api-reference/text-to-speech",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://elevenlabs.io/docs/api-reference/text-to-speech",
                "https://elevenlabs.io/docs/api-reference/authentication"
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
        "app_name": "Stability AI",
        "category": "AI/Media",
        "one_liner": "AI research organization developer of Stable Diffusion image generation models.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Developer portal allows purchase of credits for API calls self-serve.",
            "evidence_url": "https://platform.stability.ai/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://platform.stability.ai/docs/api-reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://platform.stability.ai/docs/api-reference",
                "https://platform.stability.ai/docs/getting-started/authentication"
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
        "app_name": "Canva",
        "category": "AI/Media",
        "one_liner": "Graphic design platform for creating visual content and design templates.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free account registration and self-serve developer portal.",
            "evidence_url": "https://www.canva.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://www.canva.dev/docs/connect/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://www.canva.dev/docs/connect/",
                "https://www.canva.dev/docs/connect/authentication/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 120,
            "agent_confidence": 0.93,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Figma",
        "category": "AI/Media",
        "one_liner": "Collaborative web-based design tool for vector graphics and UI prototyping.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free Starter plan and personal access token creation available.",
            "evidence_url": "https://www.figma.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://www.figma.com/developers/api",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://www.figma.com/developers/api",
                "https://www.figma.com/developers/api#authentication"
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
        "app_name": "Loom",
        "category": "AI/Media",
        "one_liner": "Video messaging extension platform for recording and sharing screen activities.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free account tier available, developer SDK signup is self-serve.",
            "evidence_url": "https://www.loom.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://dev.loom.com/docs/getting-started",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.91
        },
        "evidence": {
            "primary_docs": [
                "https://dev.loom.com/docs/getting-started",
                "https://dev.loom.com/docs/record-sdk"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.91,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Mux",
        "category": "AI/Media",
        "one_liner": "Video infrastructure service providing developer APIs for video streaming and monitoring.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free developer testing sandbox with watermarked video outputs.",
            "evidence_url": "https://www.mux.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.mux.com/api-reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.95
        },
        "evidence": {
            "primary_docs": [
                "https://docs.mux.com/api-reference",
                "https://docs.mux.com/guides/system/authentication"
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
        "app_name": "Cloudinary",
        "category": "AI/Media",
        "one_liner": "Cloud image and video storage, optimization, and media delivery platform.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 25 monthly credits.",
            "evidence_url": "https://cloudinary.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://cloudinary.com/documentation/cloudinary_references",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://cloudinary.com/documentation/cloudinary_references",
                "https://cloudinary.com/documentation/upload_images#generating_signatures"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    }
]
