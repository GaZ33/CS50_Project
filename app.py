from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm
app = Flask(__name__)




db = SQLAlchemy(app)




@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    LoginForm = LoginForm()
    if LoginForm.validate_on_submit():
        ...
    return render_template("login.html")

@app.route("/register")
def register():
    RegisterForm = RegisterForm()
    if RegisterForm.validate_on_submit():
        ...
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)