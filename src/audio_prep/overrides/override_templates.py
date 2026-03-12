"""Manual override template generation."""

from pathlib import Path

import yaml

TEMPLATE = {
    "sections": [],
    "micro_events": [],
    "notes": "Fill in overrides and keep timestamps in seconds with 3 decimals.",
}


def write_override_template(path: str | Path) -> Path:
    """Write an editable YAML override template to disk."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(TEMPLATE, sort_keys=False))
    return output_path
