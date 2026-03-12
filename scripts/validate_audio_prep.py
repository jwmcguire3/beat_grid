#!/usr/bin/env python3
"""Script wrapper for audio prep validation command."""

from audio_prep.qc.schema_validate import validate_analysis_json

if __name__ == "__main__":
    result = validate_analysis_json("data/output/analysis.json")
    print(f"valid={result}")
