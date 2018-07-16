import flask


app=Flask('MiniAmazon') # To initialise flask



products=[]

@app.route('/',methods=['GET'])
#This api is to return the index or home page of the portal
def index():
    print("Entered Index")
    return send_from_directory('static', 'Index.html')

@app.route('/api/product',methods=['GET','POST'])
def product():

    if request.method == 'GET':
        print("Enters the def for searrch with GET")
        query = request.args['name']

        for prod in products:
            if prod['name'] == query:
                print("From GET query is for: ",query)
                print("JSON Format : /n", jsonify(prod))
                return jsonify(prod)
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
        products.append(prod)
        return send_from_directory('static', 'Index.html')


app.run(host='127.0.0.1', port=5008, debug=True)
