import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo import errors

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def update_document(query, newMod):
  try:
    myUpdateResult = collection.update_one(query, newMod)
    return myUpdateResult
  except errors.DuplicateKeyError as e:
    print("Duplicated key error", e)
    return False
  except errors.WriteError as we:
    print("MongoDB returned error message", we)
    return False
  except errors.WriteConcernError as wce:
    print("MongoDB returned error message", wce)
    return False
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

def modify_doc():
  
  #request formatted data for deletion
  print('Please enter document to be updated in the form: {"key" : "value"}')
  
  #take variable for query
  try:
    myQuery = json.loads(raw_input())
  #return error if badly formatted data  
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  
  #take variable to be modified and updated 
  print('Please enter data to be updated in the form: {"key" : "value"}')
  try:
    update = json.loads(raw_input())
  #return error if badly formatted data  
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  except TypeError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  
  newUpdate = {"$set" : update}
  
  #update execution with query and modification
  myUpdateResult = update_document(myQuery, newUpdate)
  
  #if specific query exists
  if (collection.find_one(myQuery) and myUpdateResult.modified_count == 1):
    #Print raw result info (useful!) & update results
    print(dumps(myUpdateResult.raw_result))
    print("Document updated!")
  elif (collection.find_one(myQuery) and myUpdateResult.modified_count == 0):
    print(dumps(myUpdateResult.raw_result))
    print("File has already been modified.")
  else:
    #return error message
    print("Document not found.")
    
modify_doc()
