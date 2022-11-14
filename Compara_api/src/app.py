from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/usuarios')
def listar_usuario():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT correo, nombre, contrasena, cliente_empresa FROM usuarios"
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios = []
        for fila in datos:
            usuario= {'nombre':fila[0],'correo':fila[1], 'contrasena':fila[2], 'cliente_empresa': fila[3]}
            usuarios.append(usuario)
        return jsonify({'usuarios': usuarios, 'mensaje': 'Todos los usuarios'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@app.route('/usuarios/<codigo_user>', methods=['GET'])
def ver_usuario(codigo_user):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT correo, nombre, contrasena, cliente_empresa FROM usuarios WHERE codigo_user ='{0}'".format(codigo_user)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario= {'correo':datos[0], 'nombre':datos[1],'contrasena':datos[2], 'cliente_empresa': datos[3]}
            return jsonify({'usuario': usuario, 'mensaje': 'Usuario seleccionado'})
        else: 
            return jsonify({'mensaje': 'Usuario no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@app.route('/registrar', methods=['POST'])
def registrar():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO usuarios (codigo_user, nombre, correo, contrasena, cliente_empresa) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(sql, ((request.json['codigo_user']), request.json['nombre'], request.json['correo'], request.json['contrasena'], request.json['cliente_empresa'] )) 
        conexion.connection.commit()
        return jsonify({'mensaje': 'Usuario creado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@app.route('/borrar/<codigo_user>', methods=['DELETE'])
def eliminar_usuario(codigo_user):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM usuarios WHERE codigo_user ='{0}'".format(codigo_user)
        cursor.execute(sql) 
        conexion.connection.commit()
        return jsonify({'mensaje': 'Usuario eliminado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
    
@app.route('/actualizar/<codigo_user>', methods=['PUT'])
def actualizar_usuario(codigo_user):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE usuarios SET nombre=%s, correo=%s, contrasena=%s WHERE codigo_user ='{0}'".format(codigo_user)
        cursor.execute(sql, ((request.json['nombre']), request.json['correo'], request.json['contrasena'] )) 
        conexion.connection.commit()
        return jsonify({'mensaje': 'Usuario modificado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


#producto

@app.route('/registrarproducto', methods=['POST'])
def registrar_producto():
    try:
        cursor = conexion.connection.cursor()
        sql = "INSERT INTO productos (codigo_prod, nombre, precio, stock, descripcion) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(sql, ((request.json['codigo_prod']), request.json['nombre'], request.json['precio'], request.json['stock'], request.json['descripcion'] )) 
        conexion.connection.commit()
        return jsonify({'mensaje': 'Producto creado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@app.route('/productos')
def listar_producto():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre, precio, stock, descripcion FROM productos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos = []
        for fila in datos:
            producto= {'nombre':fila[0],'precio':fila[1], 'stock':fila[2], 'descripcion': fila[3]}
            productos.append(producto)
        return jsonify({'productos': producto, 'mensaje': 'Todos los productos'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@app.route('/productos/<codigo_prod>', methods=['GET'])
def ver_producto(codigo_prod):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre, precio, stock, descripcion FROM productos WHERE codigo_prod ='{0}'".format(codigo_prod)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            producto= {'nombre':datos[0], 'precio':datos[1],'stock':datos[2], 'descripcion': datos[3]}
            return jsonify({'producto': producto, 'mensaje': 'producto seleccionado'})
        else: 
            return jsonify({'mensaje': 'producto no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@app.route('/borrar_prod/<codigo_prod>', methods=['DELETE'])
def eliminar_producto(codigo_prod):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM productos WHERE codigo_prod ='{0}'".format(codigo_prod)
        cursor.execute(sql) 
        conexion.connection.commit()
        return jsonify({'mensaje': 'producto eliminado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
    
@app.route('/actualizar_prod/<codigo_prod>', methods=['PUT'])
def actualizar_producto(codigo_prod):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE productos SET nombre=%s, precio=%s, stock=%s, descripcion=%s WHERE codigo_prod ='{0}'".format(codigo_prod)
        cursor.execute(sql, ((request.json['nombre']), request.json['precio'], request.json['stock'], request.json['descripcion'] )) 
        conexion.connection.commit()
        return jsonify({'mensaje': 'producto modificado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
        

@app.route('/login', methods=['POST'])
def login():
    try:
        _json = request.json
        _correo = _json['correo']
        _pass = _json['contrasena']
        print(_pass)

        if _correo and _pass:
            return jsonify({'mensaje': 'login correcto'})
        else: 
            resp = jsonify({'mensaje': 'credenciales invalidas'})
            resp.status_code = 400
            return resp     

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})



def pagina_no_encontrada(error):
    return '<h1>La página no existe</h1>'


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()


