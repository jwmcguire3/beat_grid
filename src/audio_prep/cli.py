"""Typer CLI for Workflow 01 audio prep."""

from pathlib import Path

import typer

from audio_prep.overrides.override_templates import write_override_template
from audio_prep.qc.schema_validate import validate_analysis_json

app = typer.Typer(help="Workflow 01 audio prep scaffold CLI.")


@app.command("run")
def run_command(input_audio: Path, output_json: Path) -> None:
    """Run audio prep pipeline (stub)."""
    # TODO: wire pipeline.run_pipeline once analysis stages are implemented.
    typer.echo(f"run command is a scaffold stub. input={input_audio} output={output_json}")


@app.command("validate")
def validate_command(analysis_json: Path) -> None:
    """Validate an analysis JSON against configured schema."""
    is_valid = validate_analysis_json(analysis_json)
    if is_valid:
        typer.echo("Validation passed")
        raise typer.Exit(code=0)

    typer.echo("Validation failed")
    raise typer.Exit(code=1)


@app.command("make-overrides")
def make_overrides_command(output_path: Path) -> None:
    """Write a manual override template file."""
    path = write_override_template(output_path)
    typer.echo(f"Wrote override template: {path}")


def main() -> None:
    """Console script entrypoint."""
    app()


if __name__ == "__main__":
    main()
