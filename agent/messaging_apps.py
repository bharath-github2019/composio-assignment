# --- 3. Messaging (21-30) ---
MESSAGING_APPS = [
    {
        "app_name": "Slack",
        "category": "Messaging",
        "one_liner": "Business messaging and collaboration platform with channels, chat, and application integrations.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for workspace usage and API app development.",
            "evidence_url": "https://slack.com/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://api.slack.com/methods",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 1.0
        },
        "evidence": {
            "primary_docs": [
                "https://api.slack.com/methods",
                "https://api.slack.com/authentication",
                "https://slack.com/pricing"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers/tree/main/src/slack"
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
        "app_name": "Microsoft Teams",
        "category": "Messaging",
        "one_liner": "Workspace messaging, video meetings, and file storage collaboration tool by Microsoft.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free developer sandbox program available self-serve.",
            "evidence_url": "https://developer.microsoft.com/en-us/microsoft-365/dev-program"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Needs_Work",
            "primary_blocker": "Complex Microsoft Graph auth configurations, tenant admin permissions gates, and Microsoft Entra ID portal setups.",
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview",
                "https://learn.microsoft.com/en-us/graph/auth-v2-service"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 150,
            "agent_confidence": 0.92,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Discord",
        "category": "Messaging",
        "one_liner": "Voice, video, and text communication service popular with gaming and community servers.",
        "auth_methods": ["OAuth2", "API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free account registration and API application creation available to all users.",
            "evidence_url": "https://discord.com/developers/docs/intro"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://discord.com/developers/docs/intro",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://discord.com/developers/docs/intro",
                "https://discord.com/developers/docs/topics/oauth2"
            ],
            "secondary_sources": [
                "https://github.com/modelcontextprotocol/servers"
            ],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 100,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Telegram",
        "category": "Messaging",
        "one_liner": "Cloud-based mobile and desktop messaging app with a focus on security and speed.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Telegram Bot API tokens are free to generate via BotFather instantly.",
            "evidence_url": "https://core.telegram.org/bots"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://core.telegram.org/bots/api",
            "mcp_exists": True
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.98
        },
        "evidence": {
            "primary_docs": [
                "https://core.telegram.org/bots/api",
                "https://core.telegram.org/api/obtaining_api_id"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 90,
            "agent_confidence": 0.98,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Twilio",
        "category": "Messaging",
        "one_liner": "Customer engagement platform for SMS, voice, video, and authentication APIs.",
        "auth_methods": ["API_Key", "Basic_Auth"],
        "self_serve": {
            "value": True,
            "reason": "Free trial credit given upon signup without credit card.",
            "evidence_url": "https://www.twilio.com/try-twilio"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://www.twilio.com/docs/usage/api",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.97
        },
        "evidence": {
            "primary_docs": [
                "https://www.twilio.com/docs/usage/api",
                "https://www.twilio.com/docs/usage/security"
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
        "app_name": "SendGrid",
        "category": "Messaging",
        "one_liner": "Cloud-based customer communication platform for transactional and marketing email delivery.",
        "auth_methods": ["API_Key"],
        "self_serve": {
            "value": True,
            "reason": "Free tier available for up to 100 emails/day.",
            "evidence_url": "https://sendgrid.com/pricing/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://docs.sendgrid.com/api-reference/buying-ips/warm-up-an-ip",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.96
        },
        "evidence": {
            "primary_docs": [
                "https://docs.sendgrid.com/api-reference/buying-ips/warm-up-an-ip",
                "https://docs.sendgrid.com/for-developers/sending-email/api-getting-started"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 95,
            "agent_confidence": 0.96,
            "requires_human_review": False
        }
    },
    {
        "app_name": "WhatsApp Business",
        "category": "Messaging",
        "one_liner": "Enterprise API platform for customer engagement and messaging via WhatsApp.",
        "auth_methods": ["API_Key", "OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Meta Developer console allows self-serve test accounts and test phone numbers.",
            "evidence_url": "https://developers.facebook.com/docs/whatsapp/cloud-api"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Medium (10-50)",
            "docs_url": "https://developers.facebook.com/docs/whatsapp/cloud-api",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developers.facebook.com/docs/whatsapp/cloud-api",
                "https://developers.facebook.com/docs/whatsapp/cloud-api/get-started"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 130,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    },
    {
        "app_name": "Vonage",
        "category": "Messaging",
        "one_liner": "Global communication APIs for voice, video, SMS, and messaging channels.",
        "auth_methods": ["API_Key", "JWT"],
        "self_serve": {
            "value": True,
            "reason": "Free trial credit given upon signup without credit card.",
            "evidence_url": "https://www.vonage.com/communications-apis/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developer.vonage.com/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.93
        },
        "evidence": {
            "primary_docs": [
                "https://developer.vonage.com/",
                "https://developer.vonage.com/en/getting-started/concepts/authentication"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 115,
            "agent_confidence": 0.93,
            "requires_human_review": False
        }
    },
    {
        "app_name": "RingCentral",
        "category": "Messaging",
        "one_liner": "Cloud communications platform providing unified voice, video, and messaging APIs.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free developer account and sandbox environment.",
            "evidence_url": "https://developer.ringcentral.com/"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.ringcentral.com/api-reference",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.92
        },
        "evidence": {
            "primary_docs": [
                "https://developers.ringcentral.com/api-reference",
                "https://developers.ringcentral.com/guide/authentication/oauth"
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
        "app_name": "Zoom",
        "category": "Messaging",
        "one_liner": "Video conferencing, meetings, and team chat collaboration platform.",
        "auth_methods": ["OAuth2"],
        "self_serve": {
            "value": True,
            "reason": "Free basic account available for workspace testing and developer app creation.",
            "evidence_url": "https://zoom.us/pricing"
        },
        "api_surface": {
            "type": "REST",
            "breadth": "Broad (>50)",
            "docs_url": "https://developers.zoom.us/docs/api/",
            "mcp_exists": False
        },
        "buildability": {
            "verdict": "Ready",
            "primary_blocker": None,
            "confidence_score": 0.94
        },
        "evidence": {
            "primary_docs": [
                "https://developers.zoom.us/docs/api/",
                "https://developers.zoom.us/docs/internal-apps/s2s-oauth/"
            ],
            "secondary_sources": [],
            "extraction_timestamp": "2026-07-09T17:00:00Z"
        },
        "metadata": {
            "research_time_seconds": 110,
            "agent_confidence": 0.94,
            "requires_human_review": False
        }
    }
]
