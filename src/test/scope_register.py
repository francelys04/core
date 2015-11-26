'''
Created on 30/06/2014

@author: pet
'''
#===============================================================================
# TEST SCOPE REGISTER
#===============================================================================

import json
import simplejson
import requests

data = {}
data['codigo'] = '20349918'
data['nombre'] = 'Francelys Heredia'
result = requests.post("http://localhost:5000/registrar/cliente", data=json.dumps(data))
scope_result = result.json()
print "=========================="
print "=======TEST RESULT========"
print "=========================="
print scope_result
