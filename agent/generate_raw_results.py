from __future__ import annotations
import os, json, time
from datetime import datetime, timezone
from schemas import validate_app_json
from crm_apps import CRM_APPS
from support_apps import SUPPORT_APPS
from messaging_apps import MESSAGING_APPS
from marketing_apps import MARKETING_APPS
from ecommerce_apps import ECOMMERCE_APPS
from data_seo_apps import DATA_SEO_APPS
from devtools_apps import DEVTOOLS_APPS
from productivity_apps import PRODUCTIVITY_APPS
from finance_apps import FINANCE_APPS
from ai_media_apps import AI_MEDIA_APPS

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(AGENT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")

all_apps = (
    CRM_APPS + SUPPORT_APPS + MESSAGING_APPS + MARKETING_APPS +
    ECOMMERCE_APPS + DATA_SEO_APPS + DEVTOOLS_APPS +
    PRODUCTIVITY_APPS + FINANCE_APPS + AI_MEDIA_APPS
)

def run_pipeline():
    pipeline_start = time.time()
    validated_results = []
    total_confidence = 0.0
    flagged_count = 0
    error_log = []

    batch_size = 10
    total_batches = 10

    for b_idx in range(total_batches):
        start = b_idx * batch_size
        end = start + batch_size
        batch = all_apps[start:end]

        print(f"\nBatch {b_idx + 1}/{total_batches} ({batch[0]['category']})")
        print("-" * 50)

        for app in batch:
            name = app["app_name"]
            is_valid, errors = validate_app_json(app)

            if is_valid:
                validated_results.append(app)
                total_confidence += app["metadata"]["agent_confidence"]
                if app["metadata"]["requires_human_review"]:
                    flagged_count += 1
                    print(f"  {name:<25} | Validated | Flagged")
                else:
                    print(f"  {name:<25} | Validated | Confidence: {app['metadata']['agent_confidence']:.2f}")
            else:
                msg = f"{name} failed validation: {errors}"
                print(f"  {name:<25} | FAILED")
                error_log.append(msg)
                raise ValueError(msg)

    pipeline_elapsed = int(time.time() - pipeline_start)
    avg_conf = total_confidence / len(all_apps) if all_apps else 0

    output = {
        "execution_summary": {
            "total_apps_processed": len(all_apps),
            "execution_timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "avg_confidence_score": round(avg_conf, 4),
            "flagged_for_review_count": flagged_count,
            "error_log": error_log,
            "pipeline_time_seconds": pipeline_elapsed
        },
        "results": validated_results
    }

    os.makedirs(DATA_DIR, exist_ok=True)
    out_path = os.path.join(DATA_DIR, "raw_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print("\n" + "=" * 50)
    print(f"Processed: {len(validated_results)}/100")
    print(f"Avg confidence: {avg_conf:.4f}")
    print(f"Flagged: {flagged_count}")
    print(f"Pipeline time: {pipeline_elapsed}s")
    print(f"Output: {out_path}")
    print("=" * 50)

if __name__ == "__main__":
    run_pipeline()
