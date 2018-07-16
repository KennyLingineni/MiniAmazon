from MiniAmazon.models import db

def search_by_name(query):
    #Search for the product here
    db_query = {'name': query}
    matchingproducts = db['products'].find(db_query)  # Products is the table/collection. It returns a cursor(pointer).Cursor is a type of Generator.
    if matchingproducts:
        return list(matchingproducts) # make sure you convert the cursor to list before you send
    else:
        return []

def add_product(producttobeadded):
    #Add the Product Here
    db['products'].insert_one(producttobeadded)


def update_product(productnametobeupdated, updated_product):
    filter={'name': productnametobeupdated}
    update = {
        '$set': updated_product
    }
    # update in DB
    db['products'].update_one(filter=filter, update=update)