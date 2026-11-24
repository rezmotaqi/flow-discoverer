# SETUP

From the repository root with Python 3.12:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
python -m playwright install chromium
game-explorer doctor
game-explorer targets validate fixture
make check
```

Run `game-explorer fixture serve` to inspect the fixture manually; the server binds only to 127.0.0.1. See [CLI](CLI_REFERENCE.md).
