from pathlib import Path

from audio_prep.qc.schema_validate import validate_analysis_json


def test_schema_validate_fixture() -> None:
    assert validate_analysis_json(
        Path("tests/fixtures/sample_analysis.json"),
        Path("schemas/beat_grid_microtiming.schema.json"),
    )
