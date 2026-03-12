"""Runtime settings loading for audio prep workflow."""

from pathlib import Path

import yaml
from pydantic import BaseModel


class AudioPrepSettings(BaseModel):
    """Scaffold settings model.

    TODO: add all stage-level knobs and typed nested settings.
    """

    sample_rate_hz: int = 44100
    hop_length: int = 512
    enable_stem_separation: bool = True
    enable_micro_events: bool = True


def load_settings(path: str | Path) -> AudioPrepSettings:
    """Load settings from a YAML file."""
    content = yaml.safe_load(Path(path).read_text()) or {}
    return AudioPrepSettings(**content)
