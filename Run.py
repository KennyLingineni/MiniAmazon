import flask
from flask import Flask
from flask import request
app=Flask('temp')

# http://127.0.0.1:5005/say_hello?name=Kenny
@app.route('/say_hello',methods=['GET','POST'])
def say_hello():
    if request.method == 'GET':
        return 'HELLO ' + request.args['name']
    elif request.method == 'POST':
        return '[POST] HELLO ' + request.form['name'] + ' age ' + request.form['age']

@app.route('/say_Bye',methods=['GET'])
def say_bye():

    return 'BYE'

app.run(host='127.0.0.1',port=5009)

