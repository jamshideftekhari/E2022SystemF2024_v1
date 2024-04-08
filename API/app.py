from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/order_detail', methods=['GET'])
def get_order_detail():
    order_detail = {
        "order_id": 1001,
        "item_name": "Laptop",
        "quantity": 1,
        "unit_price": 1000,
        "country_code": "DK",
        "vat_rate": 0.25,
        "discount_rate": 0.1
    }
    return jsonify(order_detail)    

@app.route('/order_detail', methods=['POST'])
def post_order_detail():
    order_detail = request.json
    return jsonify(order_detail)

@app.route('/order', methods=['GET'])
def get_order():
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
    return jsonify(order)

@app.route('/order', methods=['POST'])
def post_order():
    order = request.json
    return jsonify(order)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Price Calculator API!"



@app.route('/vat', methods=['GET'])
def get_vat():
    vat = request.args.get('vat_number')
    response = requests.get("https://api.vatcomply.com/vat?vat_number=" + vat)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)