import os
import sys

sys.path.insert(0, os.getcwd())

import datetime
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.utils.custom_types import UserMetadataFromClient
from src.db.mongo import MongoDB
from src.utils.custom_error_handlers import MongoError
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

router = APIRouter()
DB = MongoDB()


@router.post("/send_signal_info")
async def create_one_signal_info(
    signal_info: UserMetadataFromClient, db: MongoClient = Depends(DB.get_mongo_client)
) -> JSONResponse:
    """
    Create one record of network information
    :param signal_info: Signal information from client
    :param db: DB connection
    :return: JsonResponse
    """
    try:
        mydb = db[DB.mongo_db_name]
        collection = mydb[DB.mongo_test_result_collection_name]
        signal_info.created_at = datetime.datetime.utcnow()
        signal_info.coordinate = [signal_info.longitude, signal_info.latitude]
        collection.insert_one(signal_info.dict())
        return JSONResponse(
            status_code=201,
            content=dict(
                status="OK", message="Successfully inserted the signal information"
            ),
        )

    # Thrown an error if connection to Mongo fails
    except ServerSelectionTimeoutError:
        raise MongoError(
            status_code=500,
            message="Failed to insert the signal information to DB due to timeout. "
            "Check MongoDB is running and ready to accept the connection",
        )

    except Exception as err:
        raise MongoError(
            status_code=500,
            message=f"Failed to insert the signal information to DB: {err}",
        )


@router.get("/get_signal_info/{place_id}")
async def get_signal_info_from_place_id(
    place_id: str, db: MongoClient = Depends(DB.get_mongo_client)
) -> JSONResponse:
    """
    Given place ID, return network speed and metadata
    :param place_id: Place ID from Google SDK
    :param db: DB connection
    :return: JSON Response
    """
    try:
        mydb = db[DB.mongo_db_name]
        collection = mydb[DB.mongo_search_collection_name]
        signal_info = await collection.find_one({"place_id": place_id})

        if not signal_info:
            return JSONResponse(
                status_code=400,
                content=dict(
                    status="Failed",
                    message="Requested record does not exist",
                ),
            )

        return JSONResponse(
            status_code=200,
            content=dict(
                status="OK",
                message="Successfully retrieved the signal information",
                network_speed=signal_info["network_speed"],
            ),
        )

    # Thrown an error if connection to Mongo fails
    except ServerSelectionTimeoutError:
        raise MongoError(
            status_code=500,
            message="Failed to insert the signal information to DB due to timeout. "
            "Check MongoDB is running and ready to accept the connection",
        )

    except Exception as err:
        raise MongoError(
            status_code=500,
            message=f"Failed to retrieve the signal information to DB: {err}",
        )
