"""Logging configuration helpers."""

import logging.config
from pathlib import Path

import yaml


def configure_logging(config_path: str | Path) -> None:
    """Configure standard library logging from YAML."""
    data = yaml.safe_load(Path(config_path).read_text())
    logging.config.dictConfig(data)
