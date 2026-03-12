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
        beat_grid=[BeatGridEntry(time_seconds="0.000", beat_number=1, bar_number=1)],
        micro_events=[MicroEvent(event_type="kick_hit", time_seconds="0.000", significance="high", confidence=0.8)],
        energy_curve=[EnergyPoint(time_seconds="0.000", energy=0.2)],
    )
    assert payload.song_metadata.track_id == "t1"
