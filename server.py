from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB connection string
app.config['MONGO_URI'] = 'mongodb+srv://adityav1304:aditya1234@cluster0.scwf2wk.mongodb.net/VariantControl?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Products Collection
products_collection = mongo.db.products

@app.route('/products', methods=['GET'])
def get_products():
    products = list(products_collection.find({}, {'_id': 0}))
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    products_collection.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    products_collection.update_one({'id': product_id}, {'$set': data})
    return jsonify({"message": "Product updated successfully"}), 200

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    products_collection.delete_one({'id': product_id})
    return jsonify({"message": "Product deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
