from app import render_template, redirect, url_for
from app import app



""" 
Criando rotas para páginas do site 
"""
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    LoginForm = LoginForm()
    # Quando o forms for enviado executará o if
    if LoginForm.validate_on_submit():
        ...
    return render_template("login.html", form = LoginForm)

@app.route("/register", methods=["GET", "POST"])
def register():
    RegisterForm = RegisterForm()
    # Quando o forms for enviado executará o if
    if RegisterForm.validate_on_submit():
        ...
    return render_template("register.html")