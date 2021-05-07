import json
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps
from bottle import get, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#aggregate Function
def aggregateFn(aggreg): 
  try:
    myReadResult = collection.aggregate(aggreg)
    print(myReadResult)
    #if aggregation does not equal 'None'
    if (myReadResult != None):
      #convert to json and print                 
      print("Top five shares grouped by company, strength, 200-Day SMA.")
      print(dumps(myReadResult))
    return
  except Exception as pm:
    print(dumps("MongoDB returned error message", pm))

#URI for REST service
@get('/stocks/api/v1.0/industryReport')
def read_main():

  #take value for query
  industry = request.json["Industry"]

  #aggregation filtering & projection criteria
  aggregationQ = [{"$match" : {"Industry" : {"$regex" : ".*"+industry+".*"}}}, {"$sort" : {"HighestStrength" : -1}},
                  {"$group" :  {"_id" : "$Company", "HighestStrength" : 
                   {"$max" : "$Relative Strength Index (14)"},"Highest200-DaySMA" : 
                   {"$max" : "$200-Day Simple Moving Average"}}},
                   {"$limit" : 5}]

  #if industry query doesnt exist, print error
  match = {"Industry" : {"$regex" : ".*"+industry+".*"}}
  if (collection.find(match).count() == 0):
    print("No Matches Found For:")
    print(dumps(match))
  #else send variables to aggregation function
  else: 
    myReadResult = aggregateFn(aggregationQ)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)       
    
read_main()