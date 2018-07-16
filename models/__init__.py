from pymongo import MongoClient

# To initalise pyMongo
client=MongoClient('localhost',27017) # To Connect to a MongoDB server
db=client['MiniAmazon'] # Select particular database. If its not available it gets created