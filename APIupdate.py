import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo import errors
from bottle import get, put, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['myDB']
collection = db['myCollection']

#update funtion
def update_document(query, newMod):
  try:
    myUpdateResult = collection.update_one(query, newMod)
    return myUpdateResult
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

#URI paths for REST service
@put('/stocks/api/v1.0/updateStock')
def main_update():
  ticker = request.params.get('ticker')
  myQuery = {"Ticker" : ticker}  
  modify = request.json["Volume"]
  newUpdate = {"$set" : {"Volume" : modify}}
  
  #pass query and update to update function
  myUpdateResult = update_document(myQuery, newUpdate)
  
  #if query exists & was modified
  if (collection.find_one(myQuery) and myUpdateResult.modified_count == 1):
    #print raw info & update confirmation
    print(dumps(myUpdateResult.raw_result))
    print("Document updated!")
  #if query exists & was not modified  
  elif (collection.find_one(myQuery) and myUpdateResult.modified_count == 0):
    #print raw info & info message
    print(dumps(myUpdateResult.raw_result))
    print("File has already been modified.")
  else:
    #print raw info & return error message
    print(dumps(myUpdateResult.raw_result))
    print("Document not found.")
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)  

main_update()
