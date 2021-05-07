import json
from bson import json_util
from pymongo import MongoClient
from bson.json_util import dumps
from pymongo import errors
from bottle import post, run, request
  
connection = MongoClient('localhost', 27017)
db = connection['myDB']
collection = db['myCollection']

def ins_document(document):
  try:
    myInsertResult = collection.insert_one(document)
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

@post('/create')  
def main():
    #create document by requests
    myDocument = dict()
    myDocument["id"] = request.json["id"]
    myDocument["certificate_number"] = request.json["certificate_number"]
    myDocument["business_name"] = request.json["business_name"]
    myDocument["date"] = request.json["date"]
    myDocument["result"] = request.json["result"]
    myDocument["sector"] = request.json["sector"]
    
    #insert document
    myInsertResult = ins_document(myDocument)

    #write true if inserted, false if not
    print(myInsertResult)
  
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
  
main()