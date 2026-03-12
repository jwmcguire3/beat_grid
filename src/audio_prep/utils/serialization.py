"""Serialization helpers for output payloads."""

import json
from pathlib import Path

from audio_prep.models import AudioPrepOutput


def write_output(payload: AudioPrepOutput, output_path: str | Path) -> Path:
    """Serialize a validated payload to JSON."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload.model_dump(), indent=2))
    return path
