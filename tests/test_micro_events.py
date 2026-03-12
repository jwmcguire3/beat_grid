from audio_prep.models import MicroEvent


def test_micro_event_type_literal() -> None:
    event = MicroEvent(
        event_type="drop",
        time_seconds="32.000",
        significance="medium",
        confidence=0.6,
    )
    assert event.event_type == "drop"
