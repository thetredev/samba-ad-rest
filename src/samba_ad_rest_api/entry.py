from pathlib import Path

import uvicorn

import samba_ad_rest_api.api as rest_api
from samba_ad_rest_api.config import read_config


def main(config_path: Path):
    config = read_config(config_path)

    uvicorn.run(rest_api.fastapi_entrypoint(),
        host=config.server.host,
        port=config.server.port,
        reload=config.server.reload,
        workers=config.server.workers,
        log_level=config.log.level,
    )
