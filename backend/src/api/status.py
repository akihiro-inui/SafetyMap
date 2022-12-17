from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/status")
def get_status() -> JSONResponse:
    """
    Get Web API status and return as json response
    :return: Json response contains the success status code and message
    """
    return JSONResponse(
        status_code=200,
        content=dict(
            status="OK",
            message="Service is healthy",
        ),
    )
