import importlib
from contextlib import suppress
from pathlib import Path
from typing import Iterator

from fastapi import APIRouter, FastAPI


app = FastAPI()
router_prefix=f"/{'/'.join(__name__.split('.')[1:])}"


def fastapi_entrypoint() -> str:
    for name, obj in globals().items():
        if isinstance(obj, FastAPI):
            return f"{__name__}:{name}"


def collect_routers() -> Iterator[APIRouter]:
    api_root_path = Path(__file__).parent

    for module_file in api_root_path.glob("v*/**/*.py"):
        module_path = Path(module_file.as_posix().replace("/", ".").split(__name__)[1][1:]).stem

        if module_path.endswith("__init__"):
            module_path = Path(module_path).stem

        module_path = f"{__name__}.{module_path}"
        endpoint = importlib.import_module(module_path)

        with suppress(AttributeError):
            yield getattr(endpoint, "router")


def include_routers():
    for router in collect_routers():
        app.include_router(router, prefix=router_prefix)


include_routers()
