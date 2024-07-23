from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import os
from datetime import datetime, timedelta

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

login_manager = LoginManager(app)
login_manager.login_view = "login"

login_manager.login_message_category = "info"
login_manager.login_message= "Entre ou crie em uma conta para acessar essa página!"

db = SQLAlchemy(app)


from app import routes