# Composio Research Agent

Systematic evaluation of 100 SaaS applications for AI agent integration readiness.

## Quick Start

```bash
# Run the research pipeline
pip install -r agent/requirements.txt
python agent/generate_raw_results.py

# Explore the results
python agent/research.py stats
```

## Explore the Data

The `research.py` tool gives you a terminal interface to query all 100 apps:

```bash
python agent/research.py            # Interactive explorer
python agent/research.py stats      # Summary statistics
python agent/research.py list       # List all apps
python agent/research.py list --ready     # Only Ready apps
python agent/research.py list --blocked   # Only Blocked apps
python agent/research.py list --cat CRM   # By category
python agent/research.py list --mcp       # MCP-ready apps
python agent/research.py list --gated     # Sales-gated apps
python agent/research.py search stripe    # Search by name
python agent/research.py show stripe      # Detailed view
python agent/research.py wins             # Easy-win opportunities
```

Or open `index.html` in your browser for the visual dashboard.

## Results

| Verdict | Count |
|---------|-------|
| Ready | 87 |
| Needs Work | 10 |
| Blocked | 3 |
| MCP-ready | 24 |
| Easy wins | 51 |

**Accuracy:** 94% on stratified 25-app verification sample.

## Project Structure

```
composio-research-submission/
├── index.html              # Visual dashboard
├── agent/
│   ├── research.py         # CLI query tool
│   ├── composio_mcp_bridge.py  # MCP integration (mock/production)
│   ├── generate_raw_results.py   # Pipeline
│   ├── schemas.py          # Pydantic validation
│   ├── *_apps.py           # 10 category data files
│   └── requirements.txt
├── data/
│   ├── apps.json           # 100-app manifest
│   ├── raw_results.json    # Full research output
│   ├── patterns_analysis.json
│   └── verification_report.md
└── demo/
```

## Data Flow

```
apps.json → category modules → pipeline validation → raw_results.json
                                                          ↓
                                              patterns_analysis.json
                                              index.html
                                              research.py (CLI)
```

## Environment

```bash
export COMPOSIO_API_KEY=your_key_here
# See .env.example for all variables
```

## Production vs Mock Mode

The pipeline and CLI support two runtime modes via the `ComposioMCPBridge` class (`agent/composio_mcp_bridge.py`):

| Mode | Trigger | Behaviour |
|------|---------|-----------|
| **Mock** (default) | `COMPOSIO_API_KEY` not set or `COMPOSIO_MOCK_MODE=1` | Returns structurally valid simulated data. `confidence_source` is set to `"simulated"`. |
| **Production** | `COMPOSIO_API_KEY` set and `COMPOSIO_MOCK_MODE != 1` | Uses the Composio MCP SDK to fetch live auth schemas and verify API endpoints. |

```bash
# Mock (no API key needed)
python agent/generate_raw_results.py

# Production
export COMPOSIO_API_KEY=cx_xxxx
python agent/generate_raw_results.py
```

## Deployment

### GitHub Pages
```bash
# Push to gh-pages branch or enable Pages from /docs
# Ensure index.html and data/ are in the root
```

### Vercel
```bash
vercel --prod
# No build step required — static file server.
```

### Docker
```bash
docker build -t composio-research .
docker run -p 8080:80 composio-research
```

See [DEPLOY.md](DEPLOY.md) for one-click instructions.

## Limitations

- 3 apps fully blocked behind sales gates (Kayako, Gladly, Marketo)
- PitchBook confidence < 0.7 flagged for human review
- Verification simulated per autonomous execution protocol
