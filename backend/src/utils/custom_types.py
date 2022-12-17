from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class RegisterJobRequest(BaseModel):
    array: List[int]


class UserMetadataFromClient(BaseModel):
    device_id: str
    connection_type: str
    latitude: float
    longitude: float
    download: float
    upload: float
    latency: Optional[float]
    created_at: Optional[datetime]
    coordinate: Optional[List[float]]
