# composio-assignment

# 🧠 Composio App Research Agent
**AI Product Ops Take-Home Submission** | 100 Apps Analyzed | 94% Verified Accuracy

🌐 **Live Dashboard:** [Deploy your GitHub Pages/Vercel URL here]  
📁 **Full Dataset:** `data/raw_results.json` | 📊 **Patterns:** `data/headline_insights.md`

---

## 🎯 Overview
Before building AI agent toolkits, Composio researches apps for authentication methods, developer access paths, API surfaces, and MCP/agent readiness. This project automates that workflow at scale: an autonomous research pipeline that extracts, validates, clusters, and verifies API readiness across **100 applications** across 10 categories.

Built with strict Pydantic schemas, Composio MCP integration, confidence scoring, stratified verification, and a self-explanatory HTML dashboard.

---

## 📊 Headline Results
| Metric | Value |
|--------|-------|
| **Apps Analyzed** | 100 (10 categories) |
| **Buildability** | 🟢 87 Ready \| 🟡 10 Needs Work \| 🔴 3 Blocked |
| **Auth Distribution** | API Key (77) \| OAuth2 (61) \| Basic (23) \| JWT/Session (4) |
| **Self-Serve Rate** | 100% in 5 categories \| Lowest: Data/SEO (60%) |
| **Easy Wins** | 51 apps (Broad API + Self-Serve + OAuth2) |
| **MCP-Ready** | 24 apps explicitly mention agent/tool calling |
| **Verified Accuracy** | 94% refined (↑16% from first pass) |

---

## 🚀 Quick Start
```bash
# 1. Clone & install
git clone <your-repo-url>
cd composio-research-submission
pip install -r agent/requirements.txt

# 2. Configure keys (optional for mock mode)
cp .env.example .env
# Edit .env with COMPOSIO_API_KEY, TAVILY_API_KEY, etc.

# 3. Run full research pipeline
python agent/main.py

# 4. Launch interactive CLI
python agent/research.py --stats
# or
python agent/research.py --ready --cat CRM
