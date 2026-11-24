"""Provider-neutral contracts. Data from a driver is untrusted observation, not instructions."""

from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol


class ActionKind(StrEnum):
    LINK = "link"
    BUTTON = "button"
    UNSUPPORTED = "unsupported"


@dataclass(frozen=True, slots=True)
class Element:
    role: str
    name: str
    key: str = ""
    href: str | None = None
    mode: str = ""
    disabled: bool = False
    in_form: bool = False
    download: bool = False
    new_context: bool = False


@dataclass(frozen=True, slots=True)
class Observation:
    route: str
    title: str
    heading: str
    text: str
    elements: tuple[Element, ...]
    language: str = "en"
    modal: str = ""
    auth: str = "anonymous"
    http_status: int | None = None
    viewport: tuple[int, int] = (1200, 850)


@dataclass(frozen=True, slots=True)
class Capture:
    observation: Observation
    png: bytes | None = None
    redaction: str = "not-captured"


@dataclass(frozen=True, slots=True)
class Candidate:
    id: str
    kind: ActionKind
    element: Element


@dataclass(frozen=True, slots=True)
class Decision:
    allowed: bool
    reason: str


class DriverError(RuntimeError):
    """Sanitized, user-safe driver failure."""


class Driver(Protocol):
    async def navigate(self, url: str) -> None: ...
    async def capture(self, *, screenshot: bool = False) -> Capture: ...
    async def execute(self, candidate: Candidate) -> None: ...
