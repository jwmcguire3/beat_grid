from audio_prep.models import EnergyPoint


def test_energy_point_range() -> None:
    point = EnergyPoint(time_seconds="1.000", energy=0.75)
    assert point.energy == 0.75
