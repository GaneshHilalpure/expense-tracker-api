from pydantic import BaseModel, Field
from datetime import date

class Expense(BaseModel):
    id: int
    title: str
    amount: float = Field(..., gt=0)
    category: str
    date: date