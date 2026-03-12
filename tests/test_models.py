import pytest
from pydantic import ValidationError

from audio_prep.models import AudioPrepOutput, BeatGridEntry, EnergyPoint, MicroEvent, Section, SongMetadata


def test_model_construction() -> None:
    payload = AudioPrepOutput(
        song_metadata=SongMetadata(
            track_id="t1",
            title="demo",
            duration_seconds="10.000",
            sample_rate_hz=44100,
            bpm=120.0,
            key=None,
        ),
        sections=[Section(label="intro", start_seconds="0.000", end_seconds="10.000", confidence=0.9)],
        beat_grid=[BeatGridEntry(time_seconds="0.000", beat_number=1, bar_number=1, strength="downbeat")],
        micro_events=[MicroEvent(time="0.000", type="kick_hit", section="intro", significance="high", note=None)],
        energy_curve=[EnergyPoint(time_seconds="0.000", energy=0.2)],
    )
    assert payload.song_metadata.track_id == "t1"


def test_invalid_section_label_fails_validation() -> None:
    with pytest.raises(ValidationError):
        Section(label="hook", start_seconds="0.000", end_seconds="10.000", confidence=0.9)


def test_invalid_beat_strength_fails_validation() -> None:
    with pytest.raises(ValidationError):
        BeatGridEntry(time_seconds="0.000", beat_number=1, bar_number=1, strength="accented")


def test_section_and_beat_serialization_uses_string_values() -> None:
    section = Section(label="chorus", start_seconds="1.000", end_seconds="2.000", confidence=0.7)
    beat = BeatGridEntry(time_seconds="1.000", beat_number=2, bar_number=1, strength="strong")

    assert section.model_dump() == {
        "label": "chorus",
        "start_seconds": "1.000",
        "end_seconds": "2.000",
        "confidence": 0.7,
    }
    assert beat.model_dump() == {
        "time_seconds": "1.000",
        "beat_number": 2,
        "bar_number": 1,
        "strength": "strong",
    }
