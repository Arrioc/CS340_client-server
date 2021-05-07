import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['myDB']
collection = db['myCollection']

def insert_document(document):
  try:
      result=collection.save(document)
  except ValidationError as ve:
      abort(400, str(ve))
  return result
  
def main():
  myDocument = {"id" : "0000-0000-aab2", 
                "certificate_number" : 0000001, 
                "business_name" : "Sock Business", 
                "date" : "Sep 09 2020", 
                "result" : "Negative", 
                "sector" : "Fake Ass sector - 102", 
                "address" : { 
                  "city" : "Cityville", 
                  "zip" : 49686, 
                  "street" : "Arborview Rd", 
                  "number" : 2861 }}
  
  print insert_document(myDocument)
  
main()