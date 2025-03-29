from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# uvicorn fast_api:app --reload

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float=None

@app.get("/")
def read_root():
    return {"running"}

app.get("/items/{item.id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q":q}

app.post("/items/")
def create_item(item:Item):
    return {"name": item.name, "price_with_tax":item.price +(item.tax or 0)}