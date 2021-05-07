import json
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


def aggregate(filt, proj):
  try:
    myReadResult = collection.aggregate([filt, proj])
    #if specific query exists
    if (myReadResult != None):
      #convert to json and print
      print("Total oustanding shares grouped by industry:")
      print(dumps(myReadResult))
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return


def read_main():
  
  print('Enter sector surrounded by double quotes')
  #store user sector
  try:
    sector = json.loads(raw_input())
  #return error if badly formatted data 
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  
  #store aggregation query
  filterQ = {"$match" : {"Sector" : sector}}
  projectionQ = {"$group" : {"_id" : "$Industry", "Total Outstanding Shares" : {
                    "$sum" : "$Shares Outstanding"}}}
  
  #if sector query doesnt exist, print error
  match = ({"Sector" : sector})
  if (collection.find_one(match) == None):
    print("No Matches Found For:")
    print(dumps(match))
  #else send query aggregation to aggregation function
  else:
    myReadResult = aggregate(filterQ, projectionQ)

read_main()