import json
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps
from bottle import post, route, run, request

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#read function
def read_document(document):
  try:
    myReadResult = collection.find(document)
    #if query count isnt 0
    if (myReadResult.count() != 0):
      #convert to json and print
      print(dumps(myReadResult))
    #if result found 0 matching files  
    elif (myReadResult.count() == 0):
      #return error message
      print("No Files Found With That Criteria.")
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return
  
#URI paths for REST service
@post('/stocks/api/v1.0/stockReport')
def main_read():
  #take value for query
  array = request.json["array"]
  myQuery = {"Ticker" : {"$in" : array}}
  
  #send to read funtion
  myReadResult = read_document(myQuery)
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)   

main_read()
