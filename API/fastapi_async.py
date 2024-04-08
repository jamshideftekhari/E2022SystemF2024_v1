from fastapi import FastAPI
import asyncio

app = FastAPI() 

@app.get("/")
async def home():
    return "Welcome to the Price Calculator API!"

@app.get("/order_detail")
async def get_order_detail():
    order_detail = {
        "order_id": 1001,
        "item_name": "Laptop",
        "quantity": 1,
        "unit_price": 1000,
        "country_code": "DK",
        "vat_rate": 0.25,
        "discount_rate": 0.1
    }
    return order_detail

@app.post("/order_detail")
async def post_order_detail(order_detail: dict):
    return order_detail

@app.get("/order")
async def get_order():
    order = {
        "order_id": 1001,
        "item_name": "Laptop",
        "quantity": 1,
        "unit_price": 1000,
        "subtotal": 1000,
        "vat_price": 250,
        "discount_price": 100,
        "total_price": 1150,
        "vat_id": 1,
        "discount_id": 1
    }
    return order

@app.post("/order")
async def post_order(order: dict):
    return order

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

