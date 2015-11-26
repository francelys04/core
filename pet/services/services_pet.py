'''
Created on 30/06/2014

@author: pet
'''
import re
from flask import request
from pet.restful.__init__ import services_app
from pet.data.models import *
from bson.objectid import ObjectId
from pet.services.services_resource import *
from pet.services.services_scope import *
from pet.tools.tools_general import *
from pet.tools.objects_status import *
from pet.tools.project_paths import *
import datetime

def registrar_cliente(codigo, nombre):
    cliente = Cliente(codigo=codigo, nombre=nombre)  
    cliente.save()
    return cliente.id

def buscar_cliente(id_cliente):
    cliente = Cliente.objects.get(id=ObjectId(id_cliente))
    return cliente


def registrar_mascota(codigo, nombre, fecha_nacimiento, raza, id_cliente, color, tamano):
    cliente = buscar_cliente(id_cliente)
    mascota = Mascota(cliente=cliente, codigo=codigo, nombre=nombre, fecha_nacimiento=fecha_nacimiento, raza=raza, color=color, tamano=tamano)  
    mascota.save()
    return mascota.id


def registrar_comida(codigo, nombre, marca, sabor, precio):    
    comida = Comida(codigo=codigo, nombre=nombre, marca=marca, sabor=sabor, precio=precio)  
    comida.save()
    return comida.id