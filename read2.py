import json
import pymongo
import requests
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps
from bottle import get, route, run, request, abort
from requests import HTTPError

connection = MongoClient('localhost', 27017)
db = connection['myDB']
collection = db['myCollection']


def read_document(document):
    try:
        myReadResult = collection.find_one(document)
        return myReadResult
    except errors.PyMongoError as pm:
        print("MongoDB returned error message", pm)
        abort(400, str(pm))  # errors.abort?
    return


# CURL: curl http://localhost:8080/read?business_name="ACME TEST INC."

#@get('/read')
def note_main_read():
    # Old way: myQuery = {"business_name" : "ACME TEST INC."}
    try:
        #url = 'http://localhost:8080/read?business_name="ACME TEST INC."'
        url = 'http://localhost:8080/read'
        response = requests.get(url,
                                params={'business_name' : 'ACME TEST INC.'})
        print(response)
    except HTTPError as http_err:
        print('HTTP error occurred: ', http_err)

    # debug output
    print("Debug output:")
    print(request.json)  # = "None" when run.


if __name__ == '__main__':
    # app.run(debug=True)
    run(host='localhost', port=8080)

main()