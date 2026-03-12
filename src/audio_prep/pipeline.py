"""Pipeline orchestration entrypoint.

Scaffold-only: no real DSP analysis is implemented yet.
"""

from pathlib import Path

from audio_prep.models import AudioPrepOutput


def run_pipeline(input_audio: Path, output_json: Path) -> AudioPrepOutput:
    """Run Workflow 01 pipeline.

    TODO: orchestrate ingest, analysis, QC, overrides, and serialization.
    """
    raise NotImplementedError("Pipeline analysis is not implemented in this scaffold.")
