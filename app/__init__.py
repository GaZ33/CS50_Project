from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm
import os

# Criando a aplcação com o nome do arquivo
app = Flask(__name__)

# Coping the address of my application to connect on my MySQL
db_connection = os.getenv("DB_CONNECTION2")

secret_key = os.getenv("SECRET_KEY")

# Setting the path to databse on aplication
app.config["SQLALCHEMY_DATABASE_URI"] = db_connection
# Desativa o rastreamento de modificações para evitar avisos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = secret_key

db = SQLAlchemy(app)


