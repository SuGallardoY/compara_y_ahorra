#importaciones para validaciones
from flask import flash , jsonify, make_response
import re, requests, json
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def field_validate(name_field, data):
    try:
        return data[name_field]
    except KeyError:
        return None        

class User:

    def __init__(self, data):
        self.codigo_user = field_validate('codigo_user', data)
        self.nombre = field_validate('nombre', data)
        self.correo = field_validate('correo', data)
        self.contrasena = field_validate('contrasena', data)
        self.cliente_empresa = field_validate('cliente_empresa', data)


    @classmethod
    def login(cls, formulario):
        payload = {'correo': formulario['correo'], 'contrasena': formulario['contrasena']}
        url = 'http://127.0.0.1:5000/login'
        print('url:', url)        
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        print('response: ', resp)
        return resp

    @classmethod
    def ver_usuario(cls, formulario):
        url = 'http://127.0.0.1:5000/usuarios/{0}'.format(formulario['codigo_user'])
        print('url:', url)
        resp = requests.get(url, headers=headers)
        print('response: ', resp)
        user = resp.json()
        return user

    @classmethod
    def listar_usuarios(cls):
        url = 'http://127.0.0.1:5000/usuarios'
        print('url:', url)
        resp = requests.get(url, headers=headers)
        print('response: ', resp)
        user = resp.json()
        return user

    @classmethod
    def registrar(cls, formulario):
        payload = {'nombre': formulario['nombre'], 'correo': formulario['correo'], 'contrasena': formulario['contrasena'], 'cliente_empresa': formulario['cliente_empresa']}
        url = 'http://127.0.0.1:5000/registrar'
        print('url:', url)        
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        print('response: ', resp)
        return make_response(jsonify(resp), 200)

    @classmethod
    def eliminar_usuario(cls, formulario):
        url = 'http://127.0.0.1:5000/borrar/{0}'.format(formulario['codigo_user'])
        print('url:', url)
        resp = requests.get(url, headers=headers)
        print('response: ', resp)
        user = resp.json()
        return user

    @classmethod
    def actualizar(cls, formulario):
        payload = {'codigo_user': formulario['codigo_user'], 'nombre': formulario['nombre'], 'correo': formulario['correo'], 'contrasena': formulario['contrasena'], 'cliente_empresa': formulario['cliente_empresa']}
        url = 'http://127.0.0.1:5000/actualizar/{0}'.format(formulario['codigo_user'])
        print('url:', url)        
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        print('response: ', resp)
        return resp



    



