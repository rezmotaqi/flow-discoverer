import json
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest
from typer.testing import CliRunner

from game_explorer.cli.app import app
from game_explorer.core.config import TargetConfig, load_target
from game_explorer.fixture.site import running_fixture

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs/fixture.yaml"


def test_cli(tmp_path: Path) -> None:
    runner = CliRunner()
    assert runner.invoke(app, ["--help"]).exit_code == 0
    assert runner.invoke(app, ["init", "--workspace", str(tmp_path / "artifacts")]).exit_code == 0
    assert (
        runner.invoke(app, ["targets", "validate", "fixture", "--config", str(CONFIG)]).exit_code
        == 0
    )
    assert runner.invoke(app, ["targets", "validate", "xgame"]).exit_code == 2


@pytest.mark.parametrize(
    "url",
    [
        "https://example.org/",
        "http://localhost:90/",
        "http://127.0.0.1:90/?t=x",
        "http://127.0.0.1:90@127.0.0.1:89/",
        "http://127.0.0.1:89/payment",
        "http://127.0.0.2:89/",
    ],
)
def test_config_rejects_unknown_scope(url: str) -> None:
    with pytest.raises(ValueError):
        TargetConfig.model_validate(load_target(CONFIG).model_dump() | {"start_url": url})


def test_fixture_contract() -> None:
    with running_fixture() as origin:
        for path, phrase, status in [
            ("/", "Arena Lab", 200),
            ("/fa", "امتیاز", 200),
            ("/account", "Authentication required", 401),
            ("/broken", "intentional", 404),
        ]:
            try:
                response = urlopen(origin + path, timeout=2)  # noqa: S310 — local fixture
            except HTTPError as exc:
                response = exc
            with response:
                assert response.getcode() == status
                assert phrase in response.read().decode()
        with pytest.raises(HTTPError, match="405"):
            urlopen(Request(origin + "/payment", data=b"", method="POST"), timeout=2)


def test_task_packet_and_indexes() -> None:
    command = [sys.executable, str(ROOT / "scripts/project_context.py")]
    subprocess.run([*command, "--check"], check=True, cwd=ROOT)
    packet = json.loads(subprocess.check_output([*command, "--task", "T-002"], cwd=ROOT))
    assert packet["task"]["depends"] == ["T-001"]
    assert "F-005" in {feature["id"] for feature in packet["features"]}
