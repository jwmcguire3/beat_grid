"""Pydantic contract models for Workflow 01 output.

These are scaffold models and will evolve with schema alignment.
"""

from enum import Enum

from pydantic import BaseModel, Field


class SectionLabel(str, Enum):
    """Closed vocabulary for section labels."""

    INTRO = "intro"
    VERSE = "verse"
    PRE_CHORUS = "pre_chorus"
    CHORUS = "chorus"
    POST_CHORUS = "post_chorus"
    BRIDGE = "bridge"
    BREAKDOWN = "breakdown"
    OUTRO = "outro"
    INSTRUMENTAL = "instrumental"
    AD_LIB = "ad_lib"


class BeatStrength(str, Enum):
    """Closed vocabulary for beat strengths."""

    DOWNBEAT = "downbeat"
    STRONG = "strong"
    WEAK = "weak"
    OFF = "off"


class MicroEventType(str, Enum):
    """Closed vocabulary for micro event types."""

    SNARE_HIT = "snare_hit"
    KICK_HIT = "kick_hit"
    BASS_DROP = "bass_drop"
    VOCAL_ONSET = "vocal_onset"
    VOCAL_OFFSET = "vocal_offset"
    SILENCE_START = "silence_start"
    SILENCE_END = "silence_end"
    CRASH = "crash"
    FILL_START = "fill_start"
    FILL_END = "fill_end"
    CHORD_CHANGE = "chord_change"
    BUILDUP_START = "buildup_start"
    DROP = "drop"


class Significance(str, Enum):
    """Closed vocabulary for event significance."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


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

    label: SectionLabel
    start_seconds: str
    end_seconds: str
    confidence: float = Field(ge=0.0, le=1.0)


class BeatGridEntry(BaseModel):
    """Beat grid point."""

    time_seconds: str
    beat_number: int = Field(ge=1, le=4)
    bar_number: int = Field(ge=1)
    strength: BeatStrength


class MicroEvent(BaseModel):
    """Micro-timing or musically salient event."""

    time: str
    type: MicroEventType
    section: str
    significance: Significance
    note: str | None


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
