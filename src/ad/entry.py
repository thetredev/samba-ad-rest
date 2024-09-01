import tomllib
from pathlib import Path

import uvicorn
from dotmap import DotMap

import ad.api.rest as rest_api


def read_config(path: Path) -> dict:
    with path.open("rb") as f:
        return DotMap(tomllib.load(f))


def main(config_path: Path):
    config = read_config(config_path)
    uvicorn.run(rest_api.fastapi_entrypoint(),
        host=config.server.host,
        port=config.server.port,
        reload=config.server.reload,
        workers=config.server.workers,
        log_level=config.log.level,
    )
