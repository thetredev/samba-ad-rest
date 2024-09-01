from samba_ad_rest_api.api.utils import register_endpoint_router


router = register_endpoint_router(__name__)


@router.get("/")
async def test():
    return {"message": "Hello World"}
