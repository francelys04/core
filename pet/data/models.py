'''
Created on 17/07/2015

@author: Francelys
'''
from datetime import datetime
from mongoengine import *
from pet.__init__ import *
from mongoengine import queryset_manager
from pet.tools.objects_status import *

class Cliente(db.Document):
    codigo = db.StringField()
    nombre = db.StringField()

class Mascota(db.Document):
    propietario = db.ReferenceField(Cliente)
    codigo = db.StringField()
    nombre = db.StringField()
    fecha_nacimiento = db.DateTimeField(default=datetime.now) 
    raza = db.StringField(required=True)
    color = db.StringField(required=True)
    tamano = db.StringField(required=True)
    meta = {'allow_inheritance': True}
       
class Comida(db.Document):    
    codigo = db.StringField()
    nombre = db.StringField(required=True)
    marca = db.StringField()
    sabor = db.StringField()
    precio = db.IntField(default=0)
    meta = {'allow_inheritance': True}