"""Path resolution helpers for workflow artifacts."""

from pathlib import Path


def ensure_parent(path: Path) -> Path:
    """Create parent directories for a file path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
