from fastapi import FastAPI, HTTPException
from src.models import Expense
from src.database import expenses_collection

app = FastAPI(title="Smart Expense Tracker API")


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}


@app.post("/expenses")
def add_expense(expense: Expense):
    expenses_collection.insert_one(expense.model_dump(mode="json"))
    return {"message": "Expense added successfully"}


@app.get("/expenses")
def get_expenses(category: str = None):
    expenses = list(expenses_collection.find({}, {"_id": 0}))

    if category:
        expenses = [
            expense for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses


@app.get("/expenses/total")
def total_expenses(category: str = None):

    expenses = list(expenses_collection.find({}, {"_id": 0}))

    if category:
        expenses = [
            expense for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = sum(expense["amount"] for expense in expenses)

    return {"total": total}


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    result = expenses_collection.delete_one({"id": expense_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"message": "Expense deleted successfully"}