from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'products_db'
app.config['MONGO_URL'] = 'mongodb://localhost:27017/products_db'
mongo = PyMongo(app)



@app.route('/categories',methods=['GET'])
def get_all_categories():
	data=mongo.db.Categories
	output=[]
	for q in data.find():
		output.append({'name':q.name})
		return jsonify({'result':output})


@app.route('/categories',methods=['POST'])
def add_categories():
    data = mongo.db.Categories
    name = request.json['name']
    data_id = data.insert({'name':name})
    new_data = data.find_one({'_id':data_id})
    output = {'name':new_data['name']}
    return jsonify({'result':output})



@app.route('/product/<name>',methods=['GET'])
def get_one_product(name):
    data=mongo.db.Product
    q = data.find_one({'name':name})

    if q:
	    output = {'name':q['name'],'category':q['category'],'price':q['price']}
    else:
        output = 'No result found'
    return jsonify({'result':output})


@app.route('/product',methods=['POST'])
def add_product(name):
    data = mongo.db.Product
    name = request.json['name']
    category = request.json['category']
    price = request.json['price']
    data_id = data.insert({'name':name, 'category':category, 'price':price})
    new_data = data.find_one({'_id':data_id})
    output = {'name':new_data['name'], 'category':new_data['category'], 'price':new_data['price'] }
    return jsonify({'result':output})


@app.route('/products',methods=['GET'])
def get_all_products():
	data=mongo.db.Products
	output=[]
	for q in data.find():
		output.append({'name':q['name'],'categorie':q['categorie'],'price':q['price']})
		return jsonify({'result':output})


@app.route('/greet')
def say_hello():
	return 'Hello from Server'


if __name__ == '__main__':
	app.run(debug = True)