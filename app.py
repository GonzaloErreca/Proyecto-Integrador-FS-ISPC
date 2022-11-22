from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config
# Entities:
from models.entities.User import User
# Models:
from models.ModelUser import ModelUser
# Permitirle a Flask acceder a carpetas
from flask import send_from_directory
# importar fotos
from datetime import datetime
# Poder borrar y actualizar foto
import os

# Vinculacion con FLASK
app = Flask(__name__)

# Login

csrf = CSRFProtect()
db = MySQL(app)

# Referencia a carpeta de fotos

CARPETA = os.path.join("img")
app.config['CARPETA'] = CARPETA

# Mostrar fotos en el index

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


# @app.route('/')
# def index():
#     return redirect(url_for('login'))

@app.route('/')
def web():
    return render_template('web/index.html')

@app.route('/Acerca-de')
def acerca():
    return render_template('web/acercaDe.html')

@app.route('/productos-y-servicios')
def productos():
    cursor = db.connection.cursor()
    cursor.execute("SELECT productos.id,productos.foto,productos.nombre,productos.descripcion,marca.marca,familia.familia,productos.precio,productos.stock FROM marca JOIN productos ON marca.id = productos.marca_id JOIN familia ON productos.familia_id = familia.id")
    productos = cursor.fetchall()
    db.connection.commit()
    cursor.close()
    return render_template('web/productosServicios.html', productos = productos)

@app.route('/contacto')
def contacto():
    return render_template('web/contacto.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña invalida...")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


# Crud



# Mostrar datos : Show

@app.route('/home')
@login_required
def home():
    cursor = db.connection.cursor()
    cursor.execute("SELECT productos.id,productos.foto,productos.nombre,productos.descripcion,marca.marca,familia.familia,productos.precio,productos.stock FROM marca JOIN productos ON marca.id = productos.marca_id JOIN familia ON productos.familia_id = familia.id")
    productos = cursor.fetchall()
    db.connection.commit()
    cursor.close()

    return render_template('crud/index.html',productos = productos)

# Eliminar datos

@app.route('/home/destroy/<string:id>', methods = ['GET'])
@login_required
def destroy(id):

    cursor = db.connection.cursor()

    # Borrar foto al eliminar

    cursor.execute("SELECT foto FROM productos WHERE id = %s", (id))
    fila = cursor.fetchall()
    os.remove(os.path.join("img/", fila[0][0]))
    cursor.execute("DELETE FROM productos WHERE id=%s",(id))
    db.connection.commit()
    return redirect("/home")
   
   # Editar datos

@app.route('/home/edit/<string:id>', methods = ['GET'])
@login_required
def edit(id):

    cursor1 = db.connection.cursor()
    cursor1.execute("SELECT productos.id,productos.nombre,productos.descripcion,productos.marca_id,marca.marca,productos.familia_id,familia.familia,productos.precio,productos.stock,productos.foto FROM marca JOIN productos ON marca.id = productos.marca_id JOIN familia ON productos.familia_id = familia.id WHERE productos.id = %s", (id))

    cursor2 = db.connection.cursor()
    cursor2.execute("SELECT * FROM `familia`")

    cursor3 = db.connection.cursor()
    cursor3.execute("SELECT * FROM `marca`")

    productos = cursor1.fetchall()
    familias = cursor2.fetchall()
    marcas = cursor3.fetchall()

    db.connection.commit()

    cursor1.close()
    cursor2.close()
    cursor3.close()

    return render_template('crud/edit.html', productos = productos, familias = familias, marcas = marcas)

# Actualizar datos

@app.route('/update', methods=['POST'])
@login_required
def update():
    # Guardar en variables los datos del form
    _nombre = request.form['txtNombre']
    _descripcion = request.form['txtDescripcion']
    _precio = request.form['txtPrecio']
    _stock = request.form['txtStock']
    _foto = request.files['txtFoto']
    _marca = request.form['txtMarca']
    _familia = request.form['txtFamilia']
    id = request.form['txtID']

    # Modifico solo nombre y precio
    cursor = db.connection.cursor()
    cursor.execute("UPDATE `productos` SET `nombre` = %s,`descripcion` = %s,`precio` = %s,`stock` = %s,`marca_id` = %s,`familia_id` = %s WHERE id = %s;", (_nombre, _descripcion, _precio, _stock, _marca,_familia, id))

    # Traer datos del form

    datos = (_nombre,_descripcion,_precio,_stock,_precio,_marca,_familia,id)

        # Modificar foto para poder actualizarla #

        # Validaciones

