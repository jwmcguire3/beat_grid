"""Pydantic contract models for Workflow 01 output.

These are scaffold models and will evolve with schema alignment.
"""

from pydantic import BaseModel, Field, field_validator

from audio_prep.constants import MICRO_EVENT_TYPES, SECTION_LABELS, SIGNIFICANCE_LEVELS


class SongMetadata(BaseModel):
    """Top-level metadata about the analyzed track."""

    track_id: str
    title: str
    duration_seconds: str
    sample_rate_hz: int
    bpm: float
    key: str | None = None


class Section(BaseModel):
    """Song section interval."""

    label: str
    start_seconds: str
    end_seconds: str
    confidence: float = Field(ge=0.0, le=1.0)

    @field_validator("label")
    @classmethod
    def validate_label(cls, value: str) -> str:
        if value not in SECTION_LABELS:
            raise ValueError(f"unsupported section label: {value}")
        return value


class BeatGridEntry(BaseModel):
    """Beat grid point."""

    time_seconds: str
    beat_number: int = Field(ge=1, le=4)
    bar_number: int = Field(ge=1)


class MicroEvent(BaseModel):
    """Micro-timing or musically salient event."""

    event_type: str
    time_seconds: str
    significance: str
    confidence: float = Field(ge=0.0, le=1.0)

    @field_validator("event_type")
    @classmethod
    def validate_event_type(cls, value: str) -> str:
        if value not in MICRO_EVENT_TYPES:
            raise ValueError(f"unsupported micro-event type: {value}")
        return value

    @field_validator("significance")
    @classmethod
    def validate_significance(cls, value: str) -> str:
        if value not in SIGNIFICANCE_LEVELS:
            raise ValueError(f"unsupported significance: {value}")
        return value


class EnergyPoint(BaseModel):
    """Energy curve sample."""

    time_seconds: str
    energy: float = Field(ge=0.0, le=1.0)


class AudioPrepOutput(BaseModel):
    """Full workflow output payload consumed by downstream workflows."""

    song_metadata: SongMetadata
    sections: list[Section]
    beat_grid: list[BeatGridEntry]
    micro_events: list[MicroEvent]
    energy_curve: list[EnergyPoint]
