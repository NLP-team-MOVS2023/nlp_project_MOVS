from pydantic import BaseModel
from enum import Enum

class ObjectSubject(BaseModel):
    objects: list
    subjects: list

class PredictProba(BaseModel):
    value: dict
    
class Timestamp(BaseModel):
    id: int
    timestamp: int