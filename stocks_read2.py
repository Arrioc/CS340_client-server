import json
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#query funtion
def find_industry(filt, proj):
  try:
    myReadResult = collection.find(filt, proj)
    #if specific query exists
    if (myReadResult.count() >= 1):
      #convert to json and print
      print(dumps(myReadResult))
    #if result found 0 files matching criteria 
    elif (myReadResult.count() == 0):
      #return error message
      print("No Files Found For Industry:")
      print(dumps(filt))
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return
  

def read_main():
  
  print('Enter industry surrounded by double quotes')
  #store user string
  try:
    industry = json.loads(raw_input())
  #return error if badly formatted data 
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  
  #reay query and search criteria and send to query funtion
  filterQ = {"Industry" : industry}
  projectionQ = {"Ticker" : 1, "_id" : 0}
  myReadResult = find_industry(filterQ, projectionQ)

read_main()