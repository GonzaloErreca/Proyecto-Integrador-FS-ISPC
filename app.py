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
   