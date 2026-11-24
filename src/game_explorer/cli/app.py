"""Command-line entry point."""

from pathlib import Path
from typing import Annotated

import typer
import yaml
from playwright.sync_api import Error, sync_playwright

from game_explorer.core.config import TargetConfig, load_target
from game_explorer.fixture.site import serve_fixture

app = typer.Typer(no_args_is_help=True, help="Evidence-first explorer for authorized fixture QA.")
targets_app = typer.Typer(no_args_is_help=True, help="Inspect target configuration.")
fixture_app = typer.Typer(no_args_is_help=True, help="Run the local synthetic application.")
app.add_typer(targets_app, name="targets")
app.add_typer(fixture_app, name="fixture")

DEFAULT_WORKSPACE = Path("artifacts")
DEFAULT_CONFIG = Path("configs/fixture.yaml")
Workspace = Annotated[Path, typer.Option("--workspace", help="Local artifact directory.")]
Config = Annotated[Path, typer.Option("--config", help="Fixture target YAML.")]


def fail(message: str, code: int = 1) -> typer.Exit:
    typer.echo(message, err=True)
    return typer.Exit(code)


def target_config(target: str, config: Path) -> TargetConfig:
    if target != "fixture":
        raise fail("Only the bundled synthetic fixture is enabled.", 2)
    try:
        return load_target(config)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        raise fail(f"Could not validate fixture configuration ({type(exc).__name__}).", 2) from None


@app.command()
def init(workspace: Workspace = DEFAULT_WORKSPACE) -> None:
    """Create a local workspace for exploration data."""
    try:
        workspace.mkdir(mode=0o700, parents=True, exist_ok=True)
    except OSError:
        raise fail("Cannot create the artifact workspace.") from None
    typer.echo(f"Workspace: {workspace.resolve()}")


@app.command()
def doctor() -> None:
    """Smoke-test a local Chromium launch; never contact a target or provider."""
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            browser.close()
    except Error:
        raise fail(
            "Chromium could not launch. Run: python -m playwright install chromium"
        ) from None
    typer.echo("Chromium launch: OK; target scope: bundled loopback fixture only.")


@targets_app.command("list")
def targets_list() -> None:
    """List supported targets."""
    typer.echo("fixture  Arena Lab (synthetic, internal QA)")


@targets_app.command("validate")
def targets_validate(target: str, config: Config = DEFAULT_CONFIG) -> None:
    """Validate a fixture configuration without contacting the target."""
    cfg = target_config(target, config)
    typer.echo(f"Valid: {cfg.id} ({cfg.mode}), {len(cfg.allowed_routes)} allowed routes.")


@fixture_app.command("serve")
def fixture_serve(port: Annotated[int, typer.Option(min=0, max=65535)] = 8765) -> None:
    """Host Arena Lab for manual inspection on numeric loopback only."""
    try:
        serve_fixture(port)
    except OSError:
        raise fail("Unable to bind the fixture loopback listener.") from None
