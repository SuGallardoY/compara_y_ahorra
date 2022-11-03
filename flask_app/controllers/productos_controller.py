from flask import render_template, redirect, session, request, flash
from flask_app import app
import flask_app 

#importación de modelos
from flask_app.models.users import User
from flask_app.models.productos import Producto

@app.route('/new/producto')
def new_producto():
    #validar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect('/')
        ##en session tengo el id del usuario session['user_id]
        #queremos una función que con ese id devuelva una instancia de usuario para enviarla al html

    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario)

    return render_template('new_productos.html', user=user)

##ruta a la accion del formualrio, para guardar los datos
@app.route('/create/producto', methods = ['POST'])
def create_producto():
    #validar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect('/')


    if not Producto.valida_producto(request.form):
        return redirect('/new/producto')
    


    Producto.save(request.form)

    return redirect('/dashboard')

@app.route('/edit/producto/<int:id>')
def edit_producto(id):
    if 'user_id' not in session:
        return redirect('/')
        ##en session tengo el id del usuario session['user_id]
        #queremos una función que con ese id devuelva una instancia de usuario para enviarla al html

    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario)

    #cual es la calificaicón que vamos a editar
    formulario_calificacion = {"id" : id}

    producto = Producto.get_by_id(formulario_calificacion)

    return render_template('edit_producto.html', user=user, producto = producto)

@app.route('/update/producto', methods = ['POST'])
def update_producto():
    if 'user_id' not in session:
        return redirect('/')

    #validación de la calificación
    if not Producto.valida_producto(request.form):
        return redirect('/edit/producto/'+request.form['id'])

    Producto.update(request.form)

    return redirect('/dashboard')
    
@app.route('/delete/producto/<int:id>')
def delete_producto(id):
    if 'user_id' not in session:
        return redirect('/')

    formulario = {"id": id}

    Producto.delete(formulario)

    return redirect('/dashboard')