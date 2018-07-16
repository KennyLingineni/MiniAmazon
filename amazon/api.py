from flask import Flask,request,jsonify,send_from_directory,render_template,session

from amazon import app
from models import product as product_model
from amazon.models import user as user_model

"""
do the actual configuration of flask app here
this means, adding routes and implementing the APIs
"""


#This api is to return the index or home page of the portal
@app.route('/', methods=['GET'])
def index_func():
    print("Entered Index")
    return send_from_directory('static', 'index_org.html')


@app.route('/api/product', methods=['GET', 'POST'])
def product():
    if request.method == 'GET':
        print("Enters the def for searrch with GET")
        query = request.args['name']
        results=product_model.search_by_name(query)
        return render_template( "Results.html", results=results, db_query=query) # You need to make sure you send the results as list and not cursor.

    elif request.method == 'POST':
        print("Enters the def to update with POST")
        op_type = request.form['op_type'] # This was hard coded in the html page so that the back-end would differentiate whether this request is for add or to update
        name = request.form['name'] # form is a dictionary. you fetch values for the corresponding keys.
        desc = request.form['desc']
        price = request.form['price']
        prod = {
            'name': name,
            'desc': desc,
            'price': price
        }
        print(prod)

        if op_type == 'add':
            product_model.add_product(prod)

            # take user back to admin page
            return send_from_directory('static', 'admin.html')


        elif op_type == 'update':
            updated_product = {
                'name': name,
                'desc': request.form['desc'],
                'price': request.form['price']
            }
            product_model.update_product(prod)
         # To write to the dataBase. Products is the db/
            # take user back to admin page
            return send_from_directory('static', 'index_org.html')

@app.route('/api/user', methods=['POST'])
def user():
    # to login and signup
    op_type = request.form['op_type']

    if op_type == 'login':
        username=request.form['username']
        password=request.form['password']
        success=user_model.authenticate(username, password)
        if success:
            return send_from_directory('static','home.html')
        else :
            return send_from_directory('static', 'index.html')

    elif op_type== 'signup':
        name=request.form['name']
        username=request.form['username']
        password=request.form['password']
        success = user_model.signup_username(username,password)
        if success:
            return send_from_directory('static', 'home.html')
        else:
            return send_from_directory('static', 'index.html')
    else:
        # take user back to admin page
        return send_from_directory('static', 'index.html')

