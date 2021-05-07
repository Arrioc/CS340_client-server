import json
import bson
from bson import json_util
from bottle import get, post, route, run, request, abort

# set up URI paths for REST service
@get('/hello')
def hello():
    string = request.params.get('name')
    return "{ hello : \""+string+"\" }"  

@post('/strings')
def post_strings():
    string1 = request.json["string1"]
    string2 = request.json["string2"]
    return "{ first: \""+string1+"\", second: \""+string2+"\" }"
  
if __name__ == '__main__':
    #app.run(debug=True)
    run(host='localhost', port=8080)
    