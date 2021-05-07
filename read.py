import json
import pymongo
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps
from bottle import get, route, run, request

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def read_document(document):
  try:
    myReadResult = collection.find_one(document)
    #if specific query exists
    if (myReadResult != None):
      #convert to json and print
      print(dumps(myReadResult))
    else:
      #return error message
      print("MongoDB returns \"None\", File not found")
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

@route('/read', METHOD='GET')          
def main_read():
  #take and parse url params for query
  name = request.params.get('business_name')
  name = name.replace(" ", "+")
  name2 = name.replace("+", " ")
  myQuery = {"business_name" : {'$regex': name2}}
  
  #send to read funtion and find doc
  myReadResult = read_document(myQuery)
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)   
    

main_read()
