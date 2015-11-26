'''
Created on 17/07/2015

@author: francelys
'''
from flask import request
from flask import json
from pet.restful.__init__ import services_app
from pet.tools.tools_response import *
from pet.services.services_pet import *


@services_app.route('/registrar/cliente', methods=['POST'])
def restful_cause_register():
    data = {}
    try:
        data = json.loads(request.data)
        
        #General data validation:
        if (data['codigo'] is not None and data['nombre'] is not None):            
            id_cliente = registrar_cliente(data['codigo'], data['nombre'])
        else:
            raise Exception('Debe completar los campos para regitrar cliente')
        data = {}
        data['message'] = 'ok'
        data['id_cliente'] = id_cliente
        return make_template_response(data,'general/cliente_registrar.json')
    except Exception as e:
        data = {}
        data['error'] = e
        return make_error_response(data)

    return make_error_response(data)