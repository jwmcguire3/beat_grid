"""Closed vocabularies and shared constants for output contract."""

SECTION_LABELS: tuple[str, ...] = (
    "intro",
    "verse",
    "pre_chorus",
    "chorus",
    "post_chorus",
    "bridge",
    "breakdown",
    "outro",
    "instrumental",
    "ad_lib",
)

MICRO_EVENT_TYPES: tuple[str, ...] = (
    "snare_hit",
    "kick_hit",
    "bass_drop",
    "vocal_onset",
    "vocal_offset",
    "silence_start",
    "silence_end",
    "crash",
    "fill_start",
    "fill_end",
    "chord_change",
    "buildup_start",
    "drop",
)

SIGNIFICANCE_LEVELS: tuple[str, ...] = ("high", "medium", "low")
