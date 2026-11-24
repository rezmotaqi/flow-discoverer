"""Validated first-release target scope. This is intentionally not a generic URL crawler."""

from ipaddress import ip_address
from pathlib import Path
from typing import Annotated, Literal, Self
from urllib.parse import SplitResult, urlsplit

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

Route = Annotated[str, Field(pattern=r"^/(?:[A-Za-z0-9_-]+/)*[A-Za-z0-9_-]*$")]


def loopback_url(value: str) -> SplitResult:
    if not value.isascii() or any(c.isspace() or ord(c) < 32 for c in value) or "\\" in value:
        raise ValueError("invalid fixture URL")
    url = urlsplit(value)
    if (
        url.scheme != "http"
        or url.hostname is None
        or url.username is not None
        or url.password is not None
        or url.port is None
        or url.fragment
        or "#" in value
        or "?" in value
    ):
        raise ValueError("expected an HTTP fixture URL with explicit port and no query or fragment")
    if str(ip_address(url.hostname)) != "127.0.0.1":
        raise ValueError("only numeric 127.0.0.1 is supported in the fixture release")
    if url.netloc != f"127.0.0.1:{url.port}" or not url.port:
        raise ValueError("noncanonical fixture origin")
    return url


class SettingsModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)


class Limits(SettingsModel):
    max_actions: int = Field(default=60, ge=1, le=300)
    max_actions_per_state: int = Field(default=20, ge=1, le=50)
    max_depth: int = Field(default=8, ge=0, le=20)
    max_states: int = Field(default=50, ge=1, le=200)
    max_seconds: int = Field(default=120, ge=1, le=600)
    max_artifact_bytes: int = Field(default=25_000_000, ge=1000, le=200_000_000)
    interaction_delay_ms: int = Field(default=50, ge=0, le=5000)


class Viewport(SettingsModel):
    width: int = Field(default=1200, ge=500, le=1920)
    height: int = Field(default=850, ge=500, le=1200)


class TargetConfig(SettingsModel):
    id: Literal["fixture"]
    display_name: str = Field(min_length=1, max_length=100)
    platform: Literal["browser"] = "browser"
    start_url: str
    allowed_domains: list[Literal["127.0.0.1"]]
    allowed_routes: list[Route] = Field(min_length=1, max_length=100)
    prohibited_routes: list[Route] = Field(min_length=1, max_length=100)
    allowed_buttons: dict[Route, list[Annotated[str, Field(pattern=r"^[a-z][a-z0-9-]{0,63}$")]]] = (
        Field(default_factory=dict)
    )
    mode: Literal["internal-qa"] = "internal-qa"
    languages: list[Literal["en", "fa"]] = ["en", "fa"]
    authentication: Literal["none"] = "none"
    objective: Literal["general"] = "general"
    viewport: Viewport = Field(default_factory=Viewport)
    limits: Limits = Field(default_factory=Limits)

    @property
    def origin(self) -> str:
        return f"http://{loopback_url(self.start_url).netloc}"

    @model_validator(mode="after")
    def validate_scope(self) -> Self:
        url = loopback_url(self.start_url)
        if self.allowed_domains != ["127.0.0.1"]:
            raise ValueError("fixture scope requires the single loopback domain")
        if set(self.allowed_routes) & set(self.prohibited_routes):
            raise ValueError("allowed and prohibited routes overlap")
        if url.path not in self.allowed_routes:
            raise ValueError("start route must be explicitly allowed")
        if not set(self.allowed_buttons) <= set(self.allowed_routes):
            raise ValueError("button allowlist route must be allowed")
        return self


def load_target(path: Path) -> TargetConfig:
    with path.open("rb") as stream:
        data = stream.read(65_537)
    if len(data) > 65_536:
        raise ValueError("target configuration exceeds 64 KiB")
    return TargetConfig.model_validate(yaml.safe_load(data))
