from audio_prep.utils.timefmt import format_seconds


def test_format_seconds_enforces_three_decimals() -> None:
    assert format_seconds(1) == "1.000"
    assert format_seconds(1.23456) == "1.235"
