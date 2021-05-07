import json
from bson import json_util
from bson import errors
from bson.json_util import dumps, loads
from pymongo import MongoClient
from pymongo import errors

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def insert_doc(document):
  try:
    myInsertResult = collection.insert_one(document)
    print("Document created!")
    return True
  except errors.DuplicateKeyError as e:
    print("Duplicated key error")
    return False
  except errors.WriteError as we:
    print("MongoDB returned error message")
    return False
  except errors.WriteConcernError as wce:
    print("MongoDB returned error message")
    return False
  
def create_doc():

  #create new stock document
  print('Please enter data in the form: {"key" : "value"} with "key:value" entries separated by commas')
  
  #take document key/values for insert
  try:
    stockDoc = json.loads(raw_input())
  #return error if badly formatted data 
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
    
  #insert document
  insertResult = insert_doc(stockDoc)
    
  #write true if inserted, false if not
  print(insertResult)

create_doc()
