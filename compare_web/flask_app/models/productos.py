import json
from flask import flash
from datetime import datetime
import traceback, requests

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def field_validate(name_field, data):
    try:
        return data[name_field]
    except KeyError:
        return None  

class Producto:
    
    def __init__(self, data):
        self.codigo_prod = field_validate('codigo_prod', data)
        self.nombre = field_validate('nombre', data)
        self.precio = field_validate('precio', data)
        self.stock = field_validate('stock', data)
        self.descripcion = field_validate('descripcion', data)

    def __str__(self):
        return 'codigo_prod: {0}'.format(self.codigo_prod) 

    @classmethod
    def listar_productos(cls):
        resp = requests.get('http://127.0.0.1:5000/productos', headers=headers)
        productos = resp.json()
        return productos 

    @classmethod
    def ver_producto(cls, formulario):
        url = 'http://127.0.0.1:5000/productos/{0}'.format(formulario['codigo_prod'])
        print('url:', url)
        resp = requests.get(url, headers=headers)
        print('response: ', resp)
        user = resp.json()
        return user

    @classmethod
    def registrar(cls, formulario):
        payload = {'codigo_prod': formulario['codigo_prod'], 'nombre': formulario['nombre'], 'precio': formulario['precio'], 'stock': formulario['stock'], 'descripcion': formulario['descripcion']}
        url = 'http://127.0.0.1:5000/registrarproducto'
        print('url:', url)        
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        print('response: ', resp)
        return resp

    @classmethod
    def eliminar_producto(cls, formulario):
        url = 'http://127.0.0.1:5000/borrar/{0}'.format(formulario['codigo_prod'])
        print('url:', url)
        resp = requests.get(url, headers=headers)
        print('response: ', resp)
        user = resp.json()
        return user

    @classmethod
    def actualizar(cls, formulario):
        payload = {'codigo_prod': formulario['codigo_prod'], 'nombre': formulario['nombre'], 'precio': formulario['precio'], 'stock': formulario['stock'], 'descripcion': formulario['descripcion']}
        url = 'http://127.0.0.1:5000/actualizar_producto/{0}'.format(formulario['codigo_prod'])
        print('url:', url)        
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        print('response: ', resp)
        return resp



