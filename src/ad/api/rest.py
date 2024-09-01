import importlib
from pathlib import Path

from fastapi import FastAPI
from fastapi import APIRouter


app = FastAPI()
router = APIRouter(prefix="/api/v1")


@router.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


def fastapi_entrypoint() -> str:
    for name, obj in globals().items():
        if isinstance(obj, FastAPI):
            return f"{__name__}:{name}"


def include_routers():
    app.include_router(router)
    current_path = Path(__file__).parent

    for endpoint_file in current_path.glob("endpoints/**/*.py"):
        if endpoint_file.name == "__init__.py":
            continue

        module_file = endpoint_file.relative_to(current_path)
        module_name = Path(module_file.as_posix().replace("/", ".")).stem

        endpoint = importlib.import_module(f".{module_name}", __name__[:__name__.rfind(".")])
        endpoint_router: APIRouter = getattr(endpoint, "router")

        app.include_router(endpoint_router, prefix=f"{router.prefix}")


include_routers()
