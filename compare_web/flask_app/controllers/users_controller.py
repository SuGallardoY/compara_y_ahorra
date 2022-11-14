from flask import render_template, request, redirect, session, flash 
from flask_app import app 

from flask_app.models.users import User 
from flask_app.models.productos import Producto 
import json


@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/register', methods = ['POST'])
def register():
    pwd = None
    formulario = {
        "nombre": request.form['nombre'],
        "correo": request.form['correo'],
        "contrasena": pwd,
        "cliente_empresa": request.form['cliente_empresa']
    }
   
    codigo_user = User.registrar(formulario)

    session['codigo_user'] = codigo_user

    return redirect('/templates/dashboard')



@app.route('/login' , methods=['POST'])
def login():

    resp = User.login(request.form) 

    if resp is None or resp.status_code == 401: 
       return redirect('/')
    else: 
        correo = resp.json()

    print('correo: ', correo)
   
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():

    if 'codigo_user' not in session:
        return redirect('/')
    formulario = {"codigo_user": session['codigo_user']}
    print('formulario: ', formulario)
    user = User.ver_usuario(formulario)

    productos = Producto.listar_productos()
    print('productos: ', productos)
    return render_template('templates/dashboard.html', user=user, productos = productos)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/register')
def registrar():
    return render_template('register.html')

@app.route('/dashboard')
def ir_dash():
    return render_template('dashboard.html')


