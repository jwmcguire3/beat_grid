"""JSON schema validation helpers.

Scaffold note: this module currently performs minimal structural checks and
tracks where full `jsonschema`-based validation will be wired in.
"""

import json
from pathlib import Path

REQUIRED_KEYS = {"song_metadata", "sections", "beat_grid", "micro_events", "energy_curve"}


def validate_analysis_json(
    analysis_json_path: str | Path,
    schema_path: str | Path = "schemas/beat_grid_microtiming.schema.json",
) -> bool:
    """Validate an analysis file against scaffold schema constraints.

    TODO: upgrade to strict JSON Schema draft-2020-12 validation.
    """
    analysis_payload = json.loads(Path(analysis_json_path).read_text())
    _ = json.loads(Path(schema_path).read_text())
    return REQUIRED_KEYS.issubset(analysis_payload.keys())
