'''
Created on 30/06/2014

@author: pet
'''
#===============================================================================
# TEST USER VALIDATE
#===============================================================================

import json
import simplejson
import requests

#Test configuration------------------------------------------------------------ 
global_login = 'Francelys' #Required
global_password = '123' #Required
global_app = 'Backend' #Required
#------------------------------------------------------------------------------ 

#We get a new access token
data = {}
data['login'] = global_login
data['password'] = global_password
data['app'] = global_app

result = requests.post("http://localhost:5000/user/validate", data = json.dumps(data))
validate_result = result.json()
print validate_result