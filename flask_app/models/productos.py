from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from datetime import datetime 

class Producto:
    
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.precio = data['precio']
        self.stock = data['stock']
        self.descripcion = data['descripcion']
        self.usuarios_id = data['usuarios_id']

    @staticmethod
    def valida_producto(formulario):
        es_valido = True

        #validar que el campo no esté vacío 
        if formulario['nombre'] == '':
            flash('El campo task no puede estar vacío', 'prod')
            es_valido = False


        return es_valido


    #función para agregar datos a la tabla citas
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO productos (nombre, precio, stock, descripcion, usuarios_id) VALUES(%(nombre)s, %(precio)s, %(stock)s, %(descripcion)s, %(usuarios_id)s)"
        result = connectToMySQL('compara_y_ahorra').query_db(query, formulario)
        return result 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM productos"
        results = connectToMySQL('compara_y_ahorra').query_db(query)

        productos = []

        for producto in results:
            productos.append(cls(producto))

        return productos

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM productos WHERE id = %(id)s"
        result = connectToMySQL('compara_y_ahorra').query_db(query, formulario)
        producto = cls(result[0])
        return producto


    @classmethod
    def update(cls, formulario):
        query = "UPDATE productos SET nombre = %(nombre)s, precio = %(precio)s, stock=%(stock)s, descripcion = %(descripcion)s, usuarios_id = %(usuarios_id)s WHERE id = %(id)s"
        result = connectToMySQL('compara_y_ahorra').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM productos WHERE id = %(id)s"
        result = connectToMySQL('compara_y_ahorra').query_db(query, formulario)
        return result
