from MiniAmazon.models import db

def searchbyusername(username):
    #Search if the user is existing or not
    query={'username':username}
    matchinguser=db['users'].find(query)
    if matchinguser.count():
        return matchinguser.next() # matchinguser is of type cursor.next would take to the first value
    else:
        None
    


