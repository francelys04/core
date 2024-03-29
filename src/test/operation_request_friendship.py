'''
Created on 01/07/2014

@author: pet
'''
import json
import simplejson
import requests

#Test configuration
global_login = 'f.heredia123@heybees33.com' #Required
global_password = '20349918' #Required
global_id_bee = '53b313779b560f154e13d4ea' #Required

#We get a new access token
data = {}
data['login'] = global_login
data['password'] = global_password

result = requests.post("http://localhost:5000/user/validate", data=json.dumps(data))
validate_result = result.json()

if 'access_token' in validate_result:
    
    #We create a new operation type and notification type
    data= {}
    requests.get("http://localhost:5000/operation/operation_type", data=json.dumps(data))
            
    #We create a new operation friend_request_response
    data = {}
    data['access_token'] = validate_result['access_token']
    data['id_request_friendship'] = '53b32dd79b560f214a9d8441'
    data['id_bee'] = global_id_bee
    data['operation_type'] = 'OTAF'        
    result = requests.post("http://localhost:5000/operation/friend_request/response", data=json.dumps(data))
    friend_request_result = result.json()
            
    print ""
    print "==TEST RESULT REQUEST FRIENDSHIP="
    print "=========================="
    print friend_request_result

else:
    print "Error: Failed to generate the token"
