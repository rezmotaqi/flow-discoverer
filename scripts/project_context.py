"""Generate/check project indexes and print task metadata without reading unrelated source."""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATUSES = set(
    "PLANNED READY IN_PROGRESS BLOCKED IMPLEMENTED TESTED AWAITING_ACCEPTANCE ACCEPTED DEFERRED DEPRECATED".split()
)
REQUIRED = (
    "AGENTS.md",
    "CONTEXT.md",
    "PROJECT_STATUS.md",
    "CONTEXT_HANDOFF.md",
    "README.md",
    "CHANGELOG.md",
    "docs/INDEX.md",
)
LINKS = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)\)")


def read_registry() -> dict[str, Any]:
    return json.loads((ROOT / ".project/registry.json").read_text())  # type: ignore[no-any-return]


def index_outputs(data: dict[str, Any]) -> dict[str, str]:
    def dump(value: object) -> str:
        return json.dumps(value, indent=2, ensure_ascii=False) + "\n"

    generated = {
        ".project/feature-index.json": dump({row["id"]: row for row in data["features"]}),
        ".project/task-index.json": dump({row["id"]: row for row in data["tasks"]}),
        ".project/component-index.json": dump(data["components"]),
        ".project/dependency-index.json": dump(
            {row["id"]: row["depends"] for kind in ("features", "tasks") for row in data[kind]}
        ),
    }
    for kind, fields in [
        ("features", ("milestone", "status", "priority", "owner")),
        ("tasks", ("milestone", "status")),
    ]:
        title = kind[:-1].title()
        headings = ["ID", "Name", *[f.title() for f in fields], "Dependencies", "Verification"]
        rows = [
            f"# {title} registry",
            "",
            "Generated from [registry metadata](../../.project/registry.json). Do not edit directly.",
            "",
            "| " + " | ".join(headings) + " |",
            "| " + " | ".join(["---"] * len(headings)) + " |",
        ]
        for entry in data[kind]:
            ident = entry["id"]
            link = f"[{ident}](../../{entry['spec']})" if entry.get("spec") else ident
            cells = [
                link,
                entry["name"],
                *[entry[f] for f in fields],
                ", ".join(entry["depends"]) or "—",
                "[evidence](../../" + entry["evidence"] + ")" if entry.get("evidence") else "—",
            ]
            rows.append("| " + " | ".join(cells) + " |")
        generated[f"docs/planning/{title.upper()}_REGISTRY.md"] = "\n".join(rows) + "\n"
    return generated


def check(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"required document missing: {name}")
    feature_ids = {row["id"] for row in data["features"]}
    for kind, prefix in [("features", "F"), ("tasks", "T")]:
        items = data[kind]
        ids: set[str] = set()
        graph = {row["id"]: row["depends"] for row in items}
        for row in items:
            ident, status = row["id"], row["status"]
            if ident in ids or not re.fullmatch(f"{prefix}-[0-9]{{3}}", ident):
                errors.append(f"invalid or duplicate {kind} ID: {ident}")
            ids.add(ident)
            if status not in STATUSES or not re.fullmatch(r"M[0-9]", row["milestone"]):
                errors.append(f"{ident}: invalid status or milestone")
            if not set(row["depends"]) <= graph.keys():
                errors.append(f"{ident}: unknown {kind} dependency")
            seen, todo = set(), list(row["depends"])
            while todo:
                dep = todo.pop()
                if dep == ident:
                    errors.append(f"{ident}: circular dependency")
                    break
                if dep not in seen:
                    seen.add(dep)
                    todo.extend(graph.get(dep, []))
            if not set(row.get("features", [])) <= feature_ids:
                errors.append(f"{ident}: unknown feature")
            verified = status in {"IMPLEMENTED", "TESTED", "AWAITING_ACCEPTANCE", "ACCEPTED"}
            for key in ("spec", "evidence"):
                if row.get(key) and not (ROOT / row[key]).is_file():
                    errors.append(f"{ident}: missing {key}: {row[key]}")
            if verified:
                for path in [*row.get("source", []), *row["tests"]]:
                    if not (ROOT / path).exists():
                        errors.append(f"{ident}: missing implemented path {path}")
                if not row["tests"] or not row.get("spec"):
                    errors.append(f"{ident}: missing spec or tests")
            if status in {"TESTED", "AWAITING_ACCEPTANCE", "ACCEPTED"} and not row.get("evidence"):
                errors.append(f"{ident}: missing verification evidence")
            if status == "ACCEPTED" and not row.get("acceptance_receipt"):
                errors.append(f"{ident}: missing explicit acceptance receipt")
    docs = [*ROOT.glob("*.md"), *(ROOT / "docs").rglob("*.md")]
    for doc in docs:
        text = re.sub(r"```.*?```", "", doc.read_text(), flags=re.S)
        for link in LINKS.findall(text):
            path = link.split("#", 1)[0]
            if path and ":" not in path and not (doc.parent / path).exists():
                errors.append(f"{doc.relative_to(ROOT)}: broken link {link}")
    for name, text in index_outputs(data).items():
        path = ROOT / name
        if not path.is_file() or path.read_text() != text:
            errors.append(f"stale index: {name}; run make docs-index")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--task")
    action.add_argument("--test-feature")
    action.add_argument("--generate", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = read_registry()
    if args.generate:
        for path, contents in index_outputs(data).items():
            (ROOT / path).write_text(contents)
        return 0
    if args.check:
        if errors := check(data):
            print("\n".join(errors), file=sys.stderr)
            return 1
        print("Documentation and project indexes: OK")
        return 0
    features = {value["id"]: value for value in data["features"]}
    if args.test_feature:
        feature = features.get(args.test_feature)
        if (
            not feature
            or not feature["tests"]
            or not all((ROOT / p).is_file() for p in feature["tests"])
        ):
            parser.error("unknown feature or tests not yet implemented")
        return subprocess.call([sys.executable, "-m", "pytest", *feature["tests"]], cwd=ROOT)
    task = next((value for value in data["tasks"] if value["id"] == args.task), None)
    if not task:
        parser.error("unknown task ID")
    print(
        json.dumps(
            {
                "orientation": list(REQUIRED[:3]),
                "task": task,
                "features": [features[key] for key in task["features"]],
                "acceptance_criteria": "docs/testing/ACCEPTANCE_CRITERIA.md",
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
