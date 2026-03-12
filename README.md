# beat_grid (Workflow 01: Audio Prep)

`beat_grid` is the pipeline root workflow for an AI music-video production system.

This workflow ingests a finished master track and is responsible for producing:

1. separated stems (stubbed in this scaffold)
2. beat grid
3. tempo / BPM metadata
4. section labels
5. micro-timing events
6. energy curve
7. one validated JSON analysis file

Downstream workflows consume this output contract, so schema consistency and QC validation are first-class concerns.

## What downstream workflows will consume

The primary output is a validated `AudioPrepOutput` JSON object (see `src/audio_prep/models.py`) aligned to the schema path configured in `configs/schema_paths.yaml`.

Expected downstream consumers include:
- shot planning and pacing logic
- motion/choreography timing
- lyric/event alignment
- render orchestration
- quality-control triage

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Or use Make:

```bash
make install
```

## CLI usage

```bash
audio-prep --help
audio-prep run --input-audio data/input/song.wav --output-json data/output/analysis.json
audio-prep validate --analysis-json data/output/analysis.json
audio-prep make-overrides --output-path data/output/manual_overrides.yaml
```

## Testing

```bash
pytest
```

## What is not implemented yet

This repository is intentionally scaffold-only for now.

- No real Demucs/librosa/Essentia integration yet.
- No real stem separation, beat tracking, sectioning, or key detection yet.
- QC checks are placeholder implementations with TODO notes.

The wiring, models, config, and validation hooks are in place so implementation can proceed incrementally without breaking the contract.
