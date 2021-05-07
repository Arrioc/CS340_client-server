CREATE:
curl -H "Content-Type: application/json" -X POST -d '{"Ticker" : "JK","Profit Margin" : -0.075,"Institutional Ownership" : 0.003,"EPS growth past 5 years" : 0.242,"Total Debt/Equity" : 7.46,"Current Ratio" : 0.7,"Return on Assets" : -0.074,"Sector" : "Services","P/S" : 0.06,"Change from Open" : 0.0205,"Performance (YTD)" : -0.9353,"Performance (Week)" : -0.137,"Quick Ratio" : 0.7,"P/B" : 0.82,"EPS growth quarter over quarter" : 0.119,"Performance (Quarter)" : -0.767,"200-Day Simple Moving Average" : -0.7382,"Shares Outstanding" : 0.99,"52-Week High" : -0.9308,"P/Cash" : 1,"Change" : 0.0687,"Analyst Recom" : 3,"Volatility (Week)" : 0.0996,"Country" : "USA","Return on Equity" : 6.889,"50-Day Low" : 0.1318,"Price" : 2.49,"50-Day High" : -0.7658,"Return on Investment" : -0.011,"Shares Float" : 3.09,"Industry" : "Management Services","Beta" : -2.5,"Sales growth quarter over quarter" : 9.286,"Operating Margin" : -0.017,"EPS (ttm)" : -5.97,"52-Week Low" : 0.1318,"Average True Range" : 0.37,"Company" : "Jessicus Kilbourneous Inc.","Gap" : 0.0472,"Relative Volume" : 3.24,"Volatility (Month)" : 0.0714,"Market Cap" : 2.3,"Volume" : 46666,"Gross Margin" : 0.292,"Performance (Half Year)" : -0.7376,"Relative Strength Index (14)" : 22.46,"Insider Ownership" : 0.071,"20-Day Simple Moving Average" : -0.4444,"Performance (Month)" : -0.6331,"LT Debt/Equity" : 4.11,"Average Volume" : 15.83,"EPS growth this year" : 0.791,"50-Day Simple Moving Average" : -0.589}' http://localhost:8080/stocks/api/v1.0/createStock/JK 

    
READ:
curl -H "Content-Type: application/json" -X GET -d '{"Ticker" : "JK"}' http://localhost:8080/stocks/api/v1.0/getStock    

UPDATE:
curl -H "Content-Type: application/json" -X PUT -d '{"Volume" : 47474}' http://localhost:8080/stocks/api/v1.0/updateStock?ticker="JK"
  
  
DELETE:
curl -H "Content-Type: application/json" -X DELETE -d '{"Ticker" : "JK"}' http://localhost:8080/stocks/api/v1.0/deleteStock
    
    
STOCKREPORT:
curl -H "Content-Type: application/json" -X POST -d '{"array" : ["AA", "BA", "T"]}' http://localhost:8080/stocks/api/v1.0/stockReport
    

INDUSTRYREPORT:
curl -H "Content-Type: application/json" -X GET -d '{"Industry" : "telecom"}' http://localhost:8080/stocks/api/v1.0/industryReport
    

file 'not' found  industry report curl: 
curl -H "Content-Type: application/json" -X GET -d '{"Industry" : "tetecom"}' http://localhost:8080/stocks/api/v1.0/industryReport
