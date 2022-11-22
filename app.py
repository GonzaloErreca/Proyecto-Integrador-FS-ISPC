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

