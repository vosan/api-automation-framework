from pydantic import BaseModel

class Promotion(BaseModel):
    Name: str
    Description: str
