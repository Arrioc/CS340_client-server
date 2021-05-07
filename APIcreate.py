import json
from bson import json_util
from pymongo import MongoClient
from bson.json_util import dumps
from pymongo import errors
from bottle import post, run, request, route
  
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#insert execution
def insert_document(document):
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

#URI paths for REST service
@post('/stocks/api/v1.0/createStock/')
def main_create():
    #create document by requests
    myDocument = dict()
    myDocument["Ticker"] = request.json["Ticker"]
    myDocument["Profit Margin"] = request.json["Profit Margin"]
    myDocument["Institutional Ownership"] = request.json["Institutional Ownership"]
    myDocument["EPS growth past 5 years"] = request.json["EPS growth past 5 years"]
    myDocument["Total Debt/Equity"] = request.json["Total Debt/Equity"]
    myDocument["Current Ratio"] = request.json["Current Ratio"]
    myDocument["Return on Assets"] = request.json["Return on Assets"]
    myDocument["Sector"] = request.json["Sector"]
    myDocument["P/S"] = request.json["P/S"]
    myDocument["Change from Open"] = request.json["Change from Open"]
    myDocument["Performance (YTD)"] = request.json["Performance (YTD)"]
    myDocument["Performance (Week)"] = request.json["Performance (Week)"]
    myDocument["Quick Ratio"] = request.json["Quick Ratio"]
    myDocument["P/B"] = request.json["P/B"]
    myDocument["EPS growth quarter over quarter"] = request.json["EPS growth quarter over quarter"]
    myDocument["Performance (Quarter)"] = request.json["Performance (Quarter)"]
    myDocument["200-Day Simple Moving Average"] = request.json["200-Day Simple Moving Average"]
    myDocument["Shares Outstanding"] = request.json["Shares Outstanding"]
    myDocument["52-Week High"] = request.json["52-Week High"]
    myDocument["P/Cash"] = request.json["P/Cash"]
    myDocument["Change"] = request.json["Change"]
    myDocument["Analyst Recom"] = request.json["Analyst Recom"]
    myDocument["Volatility (Week)"] = request.json["Volatility (Week)"]
    myDocument["Country"] = request.json["Country"]
    myDocument["Return on Equity"] = request.json["Return on Equity"]
    myDocument["50-Day Low"] = request.json["50-Day Low"]
    myDocument["Price"] = request.json["Price"]
    myDocument["50-Day High"] = request.json["50-Day High"]
    myDocument["Return on Investment"] = request.json["Return on Investment"]
    myDocument["Shares Float"] = request.json["Shares Float"]
    myDocument["Industry"] = request.json["Industry"]
    myDocument["Beta"] = request.json["Beta"]
    myDocument["Sales growth quarter over quarter"] = request.json["Sales growth quarter over quarter"]
    myDocument["Operating Margin"] = request.json["Operating Margin"]
    myDocument["EPS (ttm)"] = request.json["EPS (ttm)"]
    myDocument["52-Week Low"] = request.json["52-Week Low"]
    myDocument["Average True Range"] = request.json["Average True Range"]
    myDocument["Company"] = request.json["Company"]
    myDocument["Gap"] = request.json["Gap"]
    myDocument["Relative Volume"] = request.json["Relative Volume"]
    myDocument["Volatility (Month)"] = request.json["Volatility (Month)"]
    myDocument["Market Cap"] = request.json["Market Cap"]
    myDocument["Volume"] = request.json["Volume"]
    myDocument["Gross Margin"] = request.json["Gross Margin"]
    myDocument["Performance (Half Year)"] = request.json["Performance (Half Year)"]
    myDocument["Relative Strength Index (14)"] = request.json["Relative Strength Index (14)"]
    myDocument["Insider Ownership"] = request.json["Insider Ownership"]
    myDocument["20-Day Simple Moving Average"] = request.json["20-Day Simple Moving Average"]
    myDocument["Performance (Month)"] = request.json["Performance (Month)"]
    myDocument["LT Debt/Equity"] = request.json["LT Debt/Equity"]
    myDocument["Average Volume"] = request.json["Average Volume"]
    myDocument["EPS growth this year"] = request.json["EPS growth this year"]
    myDocument["50-Day Simple Moving Average"] = request.json["50-Day Simple Moving Average"]
    
    #pass tp insert function to insert document
    myInsertResult = insert_document(myDocument)

  
if __name__ == '__main__':
    run(host='localhost', port=8080)
  
main_create()