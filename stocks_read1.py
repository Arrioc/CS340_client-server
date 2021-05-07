import json
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps, loads

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#read query and print results
def moving_average(document):
  try:
    myReadResult = collection.find(document)
    #if specific query exists
    if (myReadResult != None):
      #convert to json and print
      print(dumps(myReadResult.count()))
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return
  
def read_main():
  
  print('Enter high integer for 50-Day Simple Moving Average')
  #store high value from user
  try:
    high = json.loads(raw_input())
  #return error if badly formatted data 
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"

  print('Enter low integer for 50-Day Simple Moving Average')
  #store low value from user  
  try:
    low = json.loads(raw_input())
  #return error if badly formatted data 
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  
  #take document key/values for query
  myQuery = {"50-Day Simple Moving Average" : {"$lt" : high, "$gt" : low}}

  #send query to read function
  myReadResult = moving_average(myQuery)

read_main()