import json
import bottle
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo import errors

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def delete_document(document):
  try:
    myDeleteResult = collection.delete_one(document)
    return myDeleteResult
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
  return

def delete_doc():
  
  #request formatted data for deletion
  print('Please enter data/document to be deleted in the form: {"key" : "value"}')
  
  #take variable for deletion, query it 
  try:
    myQuery = json.loads(raw_input())
  #return error if badly formatted data  
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  
  #Deletion execution with query
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
    
delete_doc()