#!/usr/bin/env python3
"""Validate analysis JSON files against the hardened audio prep JSON Schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "jsonschema is required for qc/schema_validate.py. Install with: pip install jsonschema"
    ) from exc


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_file(schema_path: Path, data_path: Path) -> int:
    schema = load_json(schema_path)
    data = load_json(data_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda err: list(err.absolute_path))

    if not errors:
        print(f"PASS: {data_path} matches {schema_path}")
        return 0

    print(f"FAIL: {data_path} does not match {schema_path}")
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        print(f" - {location}: {error.message}")

    # Cross-field continuity checks (section time ordering, membership, etc.)
    # are intentionally handled in dedicated Python validators, not JSON Schema.
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("schemas/beat_grid_microtiming.schema.json"),
        help="Path to top-level JSON Schema entrypoint.",
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        default=[
            Path("schemas/examples/hypothetical_128bpm_example.json"),
            Path("tests/fixtures/sample_analysis.json"),
        ],
        help="JSON files to validate.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    exit_code = 0
    for data_path in args.files:
        exit_code |= validate_file(args.schema, data_path)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
