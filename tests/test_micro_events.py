import pytest
from pydantic import ValidationError

from audio_prep.models import MicroEvent


def test_micro_event_type_literal() -> None:
    event = MicroEvent(
        time="32.000",
        type="drop",
        section="chorus",
        significance="medium",
        note=None,
    )
    assert event.type == "drop"


def test_invalid_micro_event_type_fails_validation() -> None:
    with pytest.raises(ValidationError):
        MicroEvent(
            time="32.000",
            type="airhorn",
            section="chorus",
            significance="medium",
            note=None,
        )


def test_invalid_significance_fails_validation() -> None:
    with pytest.raises(ValidationError):
        MicroEvent(
            time="32.000",
            type="drop",
            section="chorus",
            significance="critical",
            note=None,
        )


def test_micro_event_serialization_uses_contract_keys_and_string_values() -> None:
    event = MicroEvent(
        time="32.000",
        type="drop",
        section="chorus",
        significance="medium",
        note="transition",
    )

    dumped = event.model_dump()
    assert set(dumped.keys()) == {"time", "type", "section", "significance", "note"}
    assert dumped == {
        "time": "32.000",
        "type": "drop",
        "section": "chorus",
        "significance": "medium",
        "note": "transition",
    }
