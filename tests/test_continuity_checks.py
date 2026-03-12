from audio_prep.models import AudioPrepOutput, BeatGridEntry, EnergyPoint, MicroEvent, Section, SongMetadata
from audio_prep.qc.continuity_checks import (
    validate_beat_grid_monotonic,
    validate_beat_number_cycle,
    validate_energy_curve_range,
    validate_micro_events_within_sections,
    validate_sections_contiguous,
)


def _sample_payload() -> AudioPrepOutput:
    return AudioPrepOutput(
        song_metadata=SongMetadata(
            track_id="track",
            title="title",
            duration_seconds="5.000",
            sample_rate_hz=44100,
            bpm=120.0,
        ),
        sections=[Section(label="intro", start_seconds="0.000", end_seconds="5.000", confidence=0.9)],
        beat_grid=[BeatGridEntry(time_seconds="0.000", beat_number=1, bar_number=1)],
        micro_events=[MicroEvent(event_type="kick_hit", time_seconds="1.000", significance="low", confidence=0.8)],
        energy_curve=[EnergyPoint(time_seconds="0.000", energy=0.5)],
    )


def test_continuity_check_stubs_return_bool() -> None:
    payload = _sample_payload()
    assert validate_sections_contiguous(payload)
    assert validate_beat_grid_monotonic(payload)
    assert validate_beat_number_cycle(payload)
    assert validate_micro_events_within_sections(payload)
    assert validate_energy_curve_range(payload)
