'''
Created on 30/06/2014

@author: pet
'''
#===============================================================================
# TEST CAUSE UPDATE AVATAR
#===============================================================================

import json
import simplejson
import requests

#Test configuration------------------------------------------------------------ 
global_login = 'j.palencia@pet.com' #Required
global_password = '19104894' #Required
global_id_cause = "53bc02d4ad0e7c14c530f7d9" #Required
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
    data['id_bee'] = global_id_cause
    data['access_token'] = validate_result['access_token']
    resource = {}
    resource['name'] = "imagen.png"
    resource['text'] = "Description of the updated avatar"
    resource['binary_content']='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'
    resource['content_type']="imagen/png"
    data['resource'] = resource
    
    result = requests.post("http://localhost:5000/bee/avatar/update", data=json.dumps(data))
    cause_result = result.json()
    print "=========================="
    print "=======TEST RESULT========"
    print "=========================="
    print cause_result
    
else:
    print "Error: Failed to generate the token"