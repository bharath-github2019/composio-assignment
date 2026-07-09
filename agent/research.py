#!/usr/bin/env python3
"""
Usage:
  python research.py                    # Interactive explorer
  python research.py list              # All 100 apps
  python research.py list --ready      # Only Ready apps
  python research.py list --blocked    # Only Blocked
  python research.py list --cat CRM    # By category
  python research.py search stripe     # Search by name
  python research.py show stripe       # Detailed view
  python research.py stats             # Summary stats
  python research.py wins              # Easy wins (broad API + OAuth2 + self-serve)
"""

from __future__ import annotations
import json, os, sys, textwrap, shutil

TERM_WIDTH = shutil.get_terminal_size((80, 20)).columns
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE, "data", "raw_results.json")

def load():
    with open(DATA_PATH) as f:
        d = json.load(f)
    return d.get("results", d if isinstance(d, list) else [])

APPS = load()

def C(s, code=0):
    if not sys.stdout.isatty():
        return s
    return f"\033[{code}m{s}\033[0m"

BOLD = lambda s: C(s, 1)
DIM = lambda s: C(s, 2)
GREEN = lambda s: C(s, 32)
YELLOW = lambda s: C(s, 33)
RED = lambda s: C(s, 31)
BLUE = lambda s: C(s, 34)
MAGENTA = lambda s: C(s, 35)
CYAN = lambda s: C(s, 36)

def verdict_color(v):
    return {"Ready": GREEN, "Needs_Work": YELLOW, "Blocked": RED}.get(v, lambda s: s)(v)

def status_char(app):
    v = app["buildability"]["verdict"]
    return {"Ready": "●", "Needs_Work": "◐", "Blocked": "○"}.get(v, "?")

def trunc(s, n):
    return s if len(s) <= n else s[:n-1] + "…"

def hr(title=""):
    w = TERM_WIDTH
    if title:
        side = (w - len(title) - 4) // 2
        print(f"{'─'*max(0,side)}  {BOLD(title)}  {'─'*max(0,w-side-len(title)-4)}")
    else:
        print("─" * w)

def cmd_list(args):
    apps = APPS
    if "--ready" in args:
        apps = [a for a in apps if a["buildability"]["verdict"] == "Ready"]
    if "--blocked" in args:
        apps = [a for a in apps if a["buildability"]["verdict"] == "Blocked"]
    if "--needs-work" in args or "--needs_work" in args:
        apps = [a for a in apps if a["buildability"]["verdict"] == "Needs_Work"]
    if "--cat" in args:
        i = args.index("--cat")
        if i + 1 < len(args):
            cat = args[i + 1]
            apps = [a for a in apps if a["category"].lower() == cat.lower()]
    if "--auth" in args:
        i = args.index("--auth")
        if i + 1 < len(args):
            auth = args[i + 1].upper().replace(" ", "_")
            apps = [a for a in apps if any(auth in m for m in a["auth_methods"])]
    if "--mcp" in args:
        apps = [a for a in apps if a["api_surface"]["mcp_exists"]]
    if "--gated" in args:
        apps = [a for a in apps if not a["self_serve"]["value"]]

    if not apps:
        print(f"\n  {DIM('No apps match your filters.')}\n")
        return

    name_w = max(len(a["app_name"]) for a in apps) + 2
    cat_w = max(len(a["category"]) for a in apps) + 2
    auth_w = 22
    ss_w = 10
    api_w = 8
    ver_w = 12

    print()
    hdr = f"  {'App':<{name_w}}{'Category':<{cat_w}}{'Auth':<{auth_w}}{'Self-Serve':<{ss_w}}{'API':<{api_w}}{'Verdict':<{ver_w}}{'Conf'}"
    print(f"  {BOLD(hdr)}")
    hr()

    for a in apps:
        name = f"{status_char(a)} {a['app_name']}"
        auth = ", ".join(a["auth_methods"])
        ss = f"{'Yes' if a['self_serve']['value'] else 'No'}"
        api = a["api_surface"]["type"]
        if a["api_surface"]["mcp_exists"]:
            api += "★"  # MCP marker
        ver = verdict_color(a["buildability"]["verdict"])
        conf = f"{a['buildability']['confidence_score']:.2f}"
        print(f"  {name:<{name_w}}{a['category']:<{cat_w}}{trunc(auth, auth_w-1):<{auth_w}}{ss:<{ss_w}}{trunc(api, api_w-1):<{api_w}}{ver:<{ver_w}}{conf}")

    print(f"\n  {DIM(f'{len(apps)} apps found')}\n")

def cmd_show(args):
    if not args:
        print(f"  {RED('Usage:')} python research.py show <app_name>\n")
        return
    query = " ".join(args).lower()
    matches = [a for a in APPS if query in a["app_name"].lower()]
    if not matches:
        print(f"  {RED(f'No app matching \"{query}\"')}\n")
        return
    a = matches[0]

    hr(f" {a['app_name']} ")
    print(f"  {BOLD('Category')}:    {a['category']}")
    print(f"  {BOLD('One-liner')}:   {a['one_liner']}")
    print(f"  {BOLD('Auth')}:        {', '.join(a['auth_methods'])}")
    ss = "Self-serve" if a['self_serve']['value'] else "Gated"
    print(f"  {BOLD('Access')}:      {ss} — {a['self_serve']['reason']}")
    print(f"  {BOLD('API')}:         {a['api_surface']['type']} | {a['api_surface']['breadth']}", end="")
    if a["api_surface"]["mcp_exists"]:
        print(f" | {GREEN('MCP available')}", end="")
    print()
    print(f"  {BOLD('Verdict')}:     {verdict_color(a['buildability']['verdict'])}", end="")
    if a["buildability"]["primary_blocker"]:
        print(f" | {a['buildability']['primary_blocker']}", end="")
    print()
    print(f"  {BOLD('Confidence')}:  {a['buildability']['confidence_score']:.2f}")
    if a["metadata"]["requires_human_review"]:
        print(f"  {YELLOW('⚠ Flagged for human review')}")
    print(f"  {BOLD('Docs')}:")
    for url in a["evidence"]["primary_docs"]:
        print(f"    {DIM('→')} {url}")
    if a["evidence"]["secondary_sources"]:
        for url in a["evidence"]["secondary_sources"]:
            print(f"    {DIM('↳')} {url}")
    hr()
    print()

def cmd_search(args):
    if not args:
        print(f"  {RED('Usage:')} python research.py search <query>\n")
        return
    query = " ".join(args)
    ql = query.lower()
    matches = [a for a in APPS if ql in a["app_name"].lower() or ql in a["category"].lower() or ql in a["one_liner"].lower() or ql in " ".join(a["auth_methods"]).lower()]
    if not matches:
        print(f"  {DIM(f'No results for \"{query}\"')}\n")
        return
    print(f"\n  {BOLD(f'{len(matches)} results for \"{query}\"')}")
    print()
    for a in matches:
        print(f"  {status_char(a)} {BOLD(a['app_name']):<25} {DIM(a['category']):<12} {verdict_color(a['buildability']['verdict']):<12} conf={a['buildability']['confidence_score']:.2f}")
    print()

def cmd_stats(args):
    total = len(APPS)
    ready = sum(1 for a in APPS if a["buildability"]["verdict"] == "Ready")
    needs = sum(1 for a in APPS if a["buildability"]["verdict"] == "Needs_Work")
    blocked = sum(1 for a in APPS if a["buildability"]["verdict"] == "Blocked")
    mcp = sum(1 for a in APPS if a["api_surface"]["mcp_exists"])
    gated = sum(1 for a in APPS if not a["self_serve"]["value"])

    hr(" COMPOSIO RESEARCH SUMMARY ")
    print(f"  {BOLD('100 apps')} across 10 categories\n")
    print(f"  {GREEN('●')} Ready       {ready:>3}  ({ready*100//total}%)")
    print(f"  {YELLOW('◐')} Needs Work  {needs:>3}  ({needs*100//total}%)")
    print(f"  {RED('○')} Blocked     {blocked:>3}  ({blocked*100//total}%)")
    print(f"  {BLUE('★')} MCP-ready   {mcp:>3}")
    print(f"  {DIM('⊘')} Gated       {gated:>3}")
    print()

    hr(" BY CATEGORY ")
    cats = {}
    for a in APPS:
        cats.setdefault(a["category"], {"Ready": 0, "Needs_Work": 0, "Blocked": 0})[a["buildability"]["verdict"]] += 1
    for cat, counts in cats.items():
        r, n, b = counts["Ready"], counts["Needs_Work"], counts["Blocked"]
        bar = f"{GREEN('●') * r}{YELLOW('◐') * n}{RED('○') * b}".ljust(16)
        print(f"  {bar} {cat:<14} {r:>2}/{n:>2}/{b:>2}")
    print()

    hr(" TOP AUTH METHODS ")
    from collections import Counter
    auths = Counter()
    for a in APPS:
        for m in a["auth_methods"]:
            auths[m] += 1
    for method, count in auths.most_common():
        pct = count * 100 // total
        bar = "█" * pct + "░" * (30 - pct)
        print(f"  {bar} {method:<12} {count:>3}")
    print()

def cmd_wins(args):
    wins = [a for a in APPS
            if a["api_surface"]["breadth"] == "Broad (>50)"
            and a["self_serve"]["value"]
            and "OAuth2" in a["auth_methods"]]
    print(f"\n  {BOLD(f'{len(wins)} easy-win apps')} — Broad API + Self-serve + OAuth2\n")
    for a in wins:
        print(f"  ● {BOLD(a['app_name']):<25} {DIM(a['category']):<14} {a['api_surface']['type']:<8} {a['buildability']['confidence_score']:.2f}")
    print()

def interactive():
    print(f"\n  {BOLD('Composio Research Explorer')}  —  Type {DIM('help')} for commands, {DIM('quit')} to exit\n")
    while True:
        try:
            cmd = input(f"  {CYAN('›')} ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] in ("q", "quit", "exit"):
            break
        elif parts[0] in ("help", "?"):
            print(f"""
  {BOLD('Commands:')}
    list [--ready|--blocked|--needs-work]    List apps with optional filters
    list --cat <name>                         Filter by category
    list --auth <method>                      Filter by auth method
    list --mcp                                Only MCP-ready apps
    list --gated                              Only gated apps
    search <query>                            Search everything
    show <name>                               Detailed app view
    stats                                     Summary statistics
    wins                                      Easy-win apps
    help                                      This help
    quit                                      Exit
""")
        elif parts[0] == "list":
            cmd_list(parts[1:])
        elif parts[0] == "search":
            cmd_search(parts[1:])
        elif parts[0] in ("show", "view", "info"):
            cmd_show(parts[1:])
        elif parts[0] == "stats":
            cmd_stats([])
        elif parts[0] == "wins":
            cmd_wins([])
        else:
            print(f"  {DIM('Unknown command. Try help.')}")

if __name__ == "__main__":
    if not APPS:
        print(f"  {RED('Error:')} Could not load data from {DATA_PATH}")
        print(f"  Run the pipeline first: python agent/generate_raw_results.py\n")
        sys.exit(1)

    if len(sys.argv) == 1:
        interactive()
    else:
        cmd = sys.argv[1]
        args = sys.argv[2:]
        if cmd == "list":
            cmd_list(args)
        elif cmd in ("show", "view", "info"):
            cmd_show(args)
        elif cmd == "search":
            cmd_search(args)
        elif cmd == "stats":
            cmd_stats(args)
        elif cmd == "wins":
            cmd_wins(args)
        else:
            print(f"  Usage: python research.py <list|show|search|stats|wins>\n")
