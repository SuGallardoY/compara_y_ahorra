from flask_app.config.mysqlconnection import connectToMySQL

#importaciones para validaciones
from flask import flash 
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

class User:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.fecha_nacimiento = data['fecha_nacimiento']
        self.correo = data['correo']
        self.contrasena = data['contrasena']
        self.cliente_empresa = data['cliente_empresa']
  

    #Función estática para validaciones
    @staticmethod
    def valida_usuario(formulario):
        #formulario = DICCIONARIO con todos los names y valores que el usuario ingresa
        es_valido = True
    
    #Validamos que el nombre tenga al menos 3 caracteres

        #Verificamos que las contraseñas coincidan
        if formulario['contrasena'] != formulario['confirm_password']:
            flash('Contraseñas NO coinciden', 'registro')
            es_valido = False

        #Revisamos que email tenga el formato correcto -> Expresiones Regulares
        if not EMAIL_REGEX.match(formulario['correo']):
            flash('E-mail inválido', 'registro')
            es_valido = False

        #Consultamos si existe el correo electrónico
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s"
        results = connectToMySQL('compara_y_ahorra').query_db(query, formulario)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False
        
        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, correo, contrasena, cliente_empresa) VALUES(%(nombre)s, %(apellido)s, %(fecha_nacimiento)s, %(correo)s, %(contrasena)s, %(cliente_empresa)s)"
        result = connectToMySQL('compara_y_ahorra').query_db(query, formulario)

        return result #devuelve el id del nuevo registro que se realizó

    @classmethod
    def get_by_email(cls, formulario):
        #recibimos formulario = {email: elena@coding.com, password: 123}
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s"
        result = connectToMySQL('compara_y_ahorra').query_db(query, formulario)
        #siempre que es SELECT devuelve una lista
        if len(result) < 1: #significa que la lista está vacía y no existe ese mail
            return False
        else: 
            #Me regresa una lista con UN registro, correspondiente al usuario de ese email
            #result = [
            #    {id: 1, first_name: elena, last_name:de troya.....} -> POSICION 0
            #]
            user = cls(result[0]) #User( {id: 1, first_name: elena, last_name:de troya.....})
            return user 

    @classmethod
    def get_by_id(cls, formulario):
        #recibimos formulario = {id: 1}
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('compara_y_ahorra').query_db(query, formulario)

        user = cls(result[0]) #creamos una instnacia d User
        return user  



