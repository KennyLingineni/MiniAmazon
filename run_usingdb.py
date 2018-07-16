from flask import Flask,request,jsonify,send_from_directory
from pymongo import MongoClient

app=Flask('MiniAmazon') # To initialise flask

# To initalise pyMongo
client=MongoClient('localhost',27017) # To Connect to a MongoDB server
db=client['MiniAmazon'] # Select particular database. If its not available it gets created


#This api is to return the index or home page of the portal
@app.route('/', methods=['GET'])
def index():
    print("Entered Index")
    return send_from_directory('static', 'index.html')


@app.route('/api/product', methods=['GET', 'POST'])
def product():
    if request.method == 'GET':
        print("Enters the def for searrch with GET")
        query = request.args['name']
        db_query={'name': query}
        matchingproducts =db['products'].find(db_query) # Products is the table/collection
        #Return the First Matching Product
        for p in matchingproducts:
            p['_id']=str(p['_id']) # A query by default returns objectID. And this object ID is not supported type in jsonify.So Convert to String
            return jsonify(p) # Here we send one by one to Jsonofy. Jinga is used we can return in one go using a template.
        return 'NO Match'

    elif request.method == 'POST':
        print("Enters the def to update with POST")
        name = request.form['name']
        desc = request.form['desc']
        price = request.form['price']
        prod = {
            'name': name,
            'desc': desc,
            'price': price
        }
        print(prod)
        db['products'].insert_one(prod) # To write to the dataBase. Products is the db/
        return send_from_directory('static', 'index.html')


app.run(host='127.0.0.1', port=5008, debug=True)
