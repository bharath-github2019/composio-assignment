"""
Composio Research Agent - Verification Logic
Blind review protocol, accuracy calculation, and error taxonomy.
"""
from __future__ import annotations
import csv

def select_verification_sample(results: list[dict], n: int = 25) -> list[dict]:
    """Stratified sampling across category, confidence, auth, self-serve."""
    from collections import defaultdict
    categories = defaultdict(list)
    for app in results:
        categories[app["category"]].append(app)
    
    sample = []
    # Pick 2-3 per category
    for cat, apps in categories.items():
        count = min(3, max(2, len(apps)))
        sample.extend(apps[:count])
    
    return sample[:n]


def calculate_accuracy(verified_csv_path: str) -> Dict:
    """Calculate field-level accuracy from verification CSV."""
    with open(verified_csv_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    fields = ["auth", "self_serve", "api_type", "api_breadth", "buildability"]
    correct = {f: 0 for f in fields}
    total = len(rows)
    
    for row in rows:
        for f in fields:
            if row.get(f"match_{f}", "").lower() == "true":
                correct[f] += 1
    
    return {
        "overall": sum(correct.values()) / (total * len(fields)),
        "per_field": {f: correct[f] / total for f in fields}
    }
