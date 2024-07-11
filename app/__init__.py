from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_login import login_manager, login_user, login_required
import os
import datetime

# Carregando as variáveis do ambiente
load_dotenv()

# Criando a aplcação com o nome do arquivo
app = Flask(__name__)

# Coping the address of my application to connect on my MySQL
db_connection = os.getenv("DB_CONNECTION2")

secret_key = os.getenv("SECRET_KEY")

Bcrypt = Bcrypt(app)
# Setting the path to databse on aplication
app.config["SQLALCHEMY_DATABASE_URI"] = db_connection
# Desativa o rastreamento de modificações para evitar avisos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = secret_key

db = SQLAlchemy(app)


from app import routes