"""
Pydantic model for Promotion data.
"""
from pydantic import BaseModel

class Promotion(BaseModel):
    Name: str
    Description: str
