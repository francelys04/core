'''
Created on 20/06/2014

@author: pet
'''
import json
import requests

payload = {'login':'j.palencia@pet.com', 'password':'19104894',
           'email':'j.palencia@pet.com','full_name':'Jesus Palencia',
           'gender':'Masculino', 'type':'FRONTEND', 'birthday':None,'phone':None, 'app':'SOCIAL'}
r = requests.post("http://localhost:5000/user/register", data = json.dumps(payload))
print r.json()