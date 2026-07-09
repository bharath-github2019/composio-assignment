"""
Composio Research Agent - Entry Point
Orchestrates the research pipeline: loads apps, runs extraction, validates, outputs.
"""
import json
from schemas import validate_dataset
from generate_raw_results import run_pipeline

if __name__ == "__main__":
    run_pipeline()
