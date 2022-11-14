from flask import render_template, redirect, session, request, flash
from flask_app import app
import flask_app 

#importación de modelos
from flask_app.models.users import User
from flask_app.models.productos import Producto

@app.route('/new/producto')
def new_producto():
    if 'codigo_user' not in session:
        return redirect('/')

    formulario = {"codigo_user": session['codigo_user']}

    user = User.ver_usuario(formulario)

    return render_template('new_productos.html', user=user)


@app.route('/create/producto', methods = ['POST'])
def create_producto():
    if 'codigo_user' not in session:
        return redirect('/')


    Producto.registrar(request.form)

    return redirect('/dashboard')

@app.route('/edit/producto/<int:id>')
def edit_producto(id):
    if 'codigo_user' not in session:
        return redirect('/')


    formulario = {"codigo_user": session['codigo_user']}

    user = User.ver_usuario(formulario)

    form_prod = {"codigo_prod" : id}
    producto = Producto.ver_producto(form_prod)

    return render_template('edit_producto.html', user=user, producto = producto)

@app.route('/update/producto', methods = ['POST'])
def update_producto():
    if 'codigo_user' not in session:
        return redirect('/')

    Producto.actualizar(request.form)

    return redirect('/dashboard')
    
@app.route('/delete/producto/<int:id>')
def delete_producto(id):
    if 'codigo_user' not in session:
        return redirect('/')

    formulario = {"codigo_prod": id}

    Producto.eliminar_producto(formulario)

    return redirect('/dashboard')