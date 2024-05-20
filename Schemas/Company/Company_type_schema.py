from typing import Optional
import uuid
from pydantic import BaseModel, Field


class Company_Type_Schema(BaseModel):
    id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    name: str = Field(nullable=False, max_length= 100)
    
    class Config:
        json_schema_extra = {
            "example":{
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Vivero"
            }
        }