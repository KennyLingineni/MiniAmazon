from flask import Flask

app=Flask('MiniAmazon') # To create the app

app.secret_key = 'some"secretkey' # To enable the cookies. Session ID is sent in cookies to the server.
from amazon import api # To invoke the api file

