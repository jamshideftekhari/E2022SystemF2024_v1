from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Price Calculator API!"

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


if __name__ == '__main__':
    app.run(debug=True)