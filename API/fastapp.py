from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome to the Price Calculator API!"}

@app.get("/order_detail")
def read_order_detail():
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

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)