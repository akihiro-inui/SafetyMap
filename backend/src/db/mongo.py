import os
import pymongo
from pymongo import MongoClient
from src.utils.common_logger import LOGGER


class MongoDB:
    def __init__(self) -> None:
        # Initiate MongoDB connector
        self.mongo_host = os.environ.get("MONGO_HOST")
        self.mongo_port = os.environ.get("MONGO_PORT")
        self.mongo_user = os.environ.get("MONGO_USERNAME")
        self.mongo_password = os.environ.get("MONGO_PASSWORD")
        self.mongo_db_name = os.environ.get("MONGO_DBNAME")
        self.mongo_test_result_collection_name = os.environ.get(
            "MONGO_TEST_RESULT_COLLECTION_NAME"
        )
        self.mongo_search_collection_name = os.environ.get(
            "MONGO_SEARCH_COLLECTION_NAME"
        )
        self.mongo_connection_string = (
            f"mongodb+srv://{self.mongo_user}:{self.mongo_password}"
            f"@{self.mongo_host}/?retryWrites=true&w=majority"
        )

    async def get_mongo_client(self) -> MongoClient:
        try:
            return pymongo.MongoClient(self.mongo_connection_string)
        except Exception as err:
            LOGGER.critical(f"Failed to establish the connection to Mongo DB: {err}")
