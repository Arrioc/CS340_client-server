import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo import errors
from bottle import get, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['myDB']
collection = db['myCollection']

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

@route('/update')
def main_update(modify = "Violation Issued"):
  #take id, set up id query, then set modification
  idStr = request.query.id
  myQuery = {"id" : idStr}
  newUpdate = {"$set" : {"result" : modify}}
  
  #update execution with query and modification
  myUpdateResult = update_document(myQuery, newUpdate)
  
  #if specific query exists
  if (collection.find_one(myQuery)):
    #Print raw result info (useful!) & update results
    print(dumps(myUpdateResult.raw_result))
    print(myUpdateResult)
  else:
    #return error message
    print("MongoDB returns \"None\", File not found.")
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
    
main_update()
