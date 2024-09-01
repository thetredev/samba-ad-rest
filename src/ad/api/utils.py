from fastapi import APIRouter


def register_endpoint_router(module_name: str) -> APIRouter:
    endpoint_name = "/".join(module_name.split("endpoints")[1].split(".")[1:])
    return APIRouter(
        prefix=f"/{endpoint_name}",
        tags=[
            endpoint_name
        ]
    )
