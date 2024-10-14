from pydantic import BaseModel
from typing import List

# Определение моделей Pydantic
class Addition(BaseModel):
    additional_info: str
    additional_number: int

class EntityData(BaseModel):
    addition: Addition
    important_numbers: List[int]
    title: str
    verified: bool


