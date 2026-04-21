from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    stock: int = 0


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Get item by ID with optional query parameter"""
    items = {
        3000: {"id": 3000, "name": "Premium Item", "price": 99.99, "stock": 50},
        3001: {"id": 3001, "name": "Deluxe Item", "price": 149.99, "stock": 30},
        3002: {"id": 3002, "name": "Elite Item", "price": 199.99, "stock": 20},
    }
    if item_id in items:
        return items[item_id]
    return {"error": f"Item {item_id} not found"}


@app.post("/items/")
def create_item(item: Item):
    """Create a new item"""
    item_id = 3003  # In production, use a database with auto-increment
    total_price = item.price + (item.tax or 0)
    
    return {
        "id": item_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax,
        "stock": item.stock,
        "total_price": total_price,
        "message": "Item created successfully"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}