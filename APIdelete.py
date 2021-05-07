import json
import bottle
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo import errors
from bottle import delete, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['myDB']
collection = db['myCollection']

#delete funtionn
def delete_document(document):
  try:
    myDeleteResult = collection.delete_one(document)
    return myDeleteResult
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
  return

@delete('/stocks/api/v1.0/deleteStock')
def delete_doc():
  #take value for deletion, query key/value
  ticker = request.json["Ticker"]
  myQuery = {"Ticker" : ticker}
  
  #pass query to delete funtion
  myDeleteResult = delete_document(myQuery)
  
  #if delete count isnt 1
  if (myDeleteResult.deleted_count != 1):
    #print error message
    print(dumps(myDeleteResult.raw_result))
    print("Document not found.")
  else:
    #return confirmation results
    print(dumps(myDeleteResult.raw_result))
    print("Document removed!")
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)    
    
delete_doc()