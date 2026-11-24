PYTHON ?= python
.PHONY: check test lint typecheck docs-check docs-index context project-status test-feature
check: lint typecheck docs-check test
test:
	$(PYTHON) -m pytest
lint:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m ruff format --check .
typecheck:
	$(PYTHON) -m mypy
docs-check:
	$(PYTHON) scripts/project_context.py --check
docs-index:
	$(PYTHON) scripts/project_context.py --generate
context:
	$(PYTHON) scripts/project_context.py --task "$(TASK)"
project-status:
	@cat PROJECT_STATUS.md
test-feature:
	$(PYTHON) scripts/project_context.py --test-feature "$(FEATURE)"
