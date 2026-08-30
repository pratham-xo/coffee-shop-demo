from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.db import db, get_database_url
from backend.models import Product, Order


app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/products", methods=["GET"])
def get_products():
    products = Product.query.all()

    return jsonify([
        {
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
        for product in products
    ])


@app.route("/api/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not product_id or not quantity:
        return jsonify({
            "error": "product_id and quantity are required"
        }), 400

    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    order = Order(
        product_id=product_id,
        quantity=quantity
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({
        "message": "Order created successfully",
        "order_id": order.id
    }), 201


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
