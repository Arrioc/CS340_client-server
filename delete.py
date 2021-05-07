import json
import bottle
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo import errors
from bottle import get, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['city']
collection = db['inspections']

def delete_document(document):
  try:
    myDeleteResult = collection.delete_one(document)
    return myDeleteResult
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
  return

@route('/delete', METHOD='GET')
def main_delete():
  #take variable for deletion, query it
  idStr = request.query.id
  myQuery = {"id" : idStr}
  
  #Deletion execution with query
  myDeleteResult = delete_document(myQuery)
  
  #if delete count isnt 1
  if (myDeleteResult.deleted_count != 1):
    #print error message
    print(dumps(myDeleteResult.raw_result))
    print("File not found")
  else:
    #return confirmation results
    print(dumps(myDeleteResult.raw_result))
    print(myDeleteResult)
    print("Document removed!")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
    
main_delete()