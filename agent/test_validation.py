from schemas import validate_app_json

stripe_data = {
  "app_name": "Stripe",
  "category": "Ecommerce",
  "one_liner": "Payment processing platform for internet businesses with comprehensive financial APIs.",
  "auth_methods": ["API_Key", "OAuth2"],
  "self_serve": {
    "value": True,
    "reason": "Free account signup with no sales contact required. Pay-as-you-go pricing with no monthly fees for basic use. Free test/sandbox mode for development.",
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
    "primary_blocker": "None",  # Test "None" cleanup
    "confidence_score": 1.0
  },
  "evidence": {
    "primary_docs": [
      "https://docs.stripe.com/api",
      "https://docs.stripe.com/api/authentication",
      "https://stripe.com/pricing",
      "https://docs.stripe.com/mcp"
    ],
    "secondary_sources": [
      "https://github.com/stripe/ai",
      "https://mcp.stripe.com"
    ],
    "extraction_timestamp": "2026-07-09T11:26:30Z"
  },
  "metadata": {
    "research_time_seconds": 130,
    "agent_confidence": 0.98,
    "requires_human_review": False
  }
}

pitchbook_data = {
  "app_name": "PitchBook",
  "category": "Data/SEO",
  "one_liner": "Financial data platform for private and public capital markets intelligence.",
  "auth_methods": ["API_Key"],
  "self_serve": {
    "value": False,
    "reason": "No free tier or self-serve signup. API access requires an existing PitchBook enterprise subscription, a separate contract agreement, and purchasing API credits through a sales representative.",
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
    "primary_blocker": "No self-serve access. API requires enterprise contract, sales-gated API key provisioning, and credit-based usage billing. Full API documentation is proprietary and not publicly accessible.",
    "confidence_score": 0.85
  },
  "evidence": {
    "primary_docs": [
      "https://pitchbook.com/data/direct-data",
      "https://api.pitchbook.com"
    ],
    "secondary_sources": [
      "https://dlthub.com/docs/dlt-ecosystem/verified-sources/pitchbook",
      "https://www.postman.com/pitchbook"
    ],
    "extraction_timestamp": "2026-07-09T11:26:00Z"
  },
  "metadata": {
    "research_time_seconds": 120,
    "agent_confidence": 0.85,
    "requires_human_review": True
  }
}

slack_data = {
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
    "extraction_timestamp": "2026-07-09T16:58:00Z"
  },
  "metadata": {
    "research_time_seconds": 150,
    "agent_confidence": 1.0,
    "requires_human_review": False
  }
}

for name, data in [("Stripe", stripe_data), ("Slack", slack_data), ("PitchBook", pitchbook_data)]:
    is_valid, errors = validate_app_json(data)
    if is_valid:
        print(f"✅ {name} validation PASSED")
    else:
        print(f"❌ {name} validation FAILED:")
        for err in errors:
            print(f"  - {err}")
