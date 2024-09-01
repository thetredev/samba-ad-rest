import tomllib
from pathlib import Path
from dataclasses import dataclass

from dotmap import DotMap


@dataclass
class ServerConnection:
    host: str
    port: int


def read_config(path: Path) -> DotMap:
    with path.open("rb") as f:
        return DotMap(tomllib.load(f))
