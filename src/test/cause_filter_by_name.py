'''
Created on 18/07/2014

@author: pet
'''
#===============================================================================
# TEST CELEBRITY FILTER BY NAME
#===============================================================================

import json
import simplejson
import requests
from pet.tools.objects_status import *

#Test configuration------------------------------------------------------------ 
global_login = 'j.palencia@pet.com' #Required
global_password = '19104894' #Required
global_status = STATUS_OBJECT_ACTIVE #Required
global_page_number = 1 #Required
global_page_size = 7 #Required
global_name_filter = "o"
#------------------------------------------------------------------------------ 

#We get a new access token
data = {}
data['login'] = global_login
data['password'] = global_password

result = requests.post("http://localhost:5000/user/validate", data=json.dumps(data))
validate_result = result.json()

if 'access_token' in validate_result:
    print "access_token: " + validate_result['access_token']
        
    #Cause data:
    data = {}
    data['access_token'] = validate_result['access_token']
    data['page_number'] = global_page_number
    data['page_size'] = global_page_size
    data['name_filter'] = global_name_filter
    data['status'] = STATUS_OBJECT_ACTIVE
    #data['device'] = "Mobile"
    
    result = requests.get("http://localhost:5000/celebrity/filter/by_name", params=data)
    cause_result = result.json()
    print "=========================="
    print "=======TEST RESULT========"
    print "=========================="
    print cause_result
    
else:
    print "Error: Failed to generate the token"