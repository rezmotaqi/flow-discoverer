# TROUBLESHOOTING

After installing Playwright, install Chromium with `python -m playwright install chromium`. If Chromium reports missing shared libraries, consult its printed installation guidance. Run `game-explorer doctor` to isolate browser launch from fixture problems. A config error prints an error class, not potentially sensitive YAML values.
