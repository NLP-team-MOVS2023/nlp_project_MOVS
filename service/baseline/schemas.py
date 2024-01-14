from pydantic import BaseModel
from enum import Enum

class ObjectSubject(BaseModel):
    object: str
    subject: str

class PredictProba(BaseModel):
    value: float
    
class Timestamp(BaseModel):
    id: int
    timestamp: int