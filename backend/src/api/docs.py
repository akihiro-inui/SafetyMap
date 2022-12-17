from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/")
def get_docs() -> RedirectResponse:
    """
    Return Swagger document HTNL
    :return: HTML shows endpoints contracts and playground
    """
    return RedirectResponse(url="/docs/")
