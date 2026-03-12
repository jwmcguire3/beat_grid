#!/usr/bin/env python3
"""Export a manual override template file."""

from audio_prep.overrides.override_templates import write_override_template

if __name__ == "__main__":
    path = write_override_template("data/output/manual_overrides.yaml")
    print(path)
