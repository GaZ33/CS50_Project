from app import render_template, redirect, url_for, request
from app import app, login_user, login_required
from app.models import Account, Information, Employees
from app.forms import LoginForm, RegisterForm



""" 
Criando rotas para páginas do site 
"""
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    loginform = LoginForm()
    # Quando o forms for enviado executará o if
    if loginform.validate_on_submit():
        attempted_user = Account.query.filter_by(Username=loginform.Username.data)
        if attempted_user and attempted_user.check_password(loginform.Password.data):
            login_user(attempted_user)
            print('a')
    return render_template("login.html", form = loginform)

@app.route("/register", methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    # Quando o forms for enviado executará o if
    if request.method == 'POST':
        if registerform.validate_on_submit():
            user_create = Account(Username=registerform.Username.data, Password=registerform.Password1.data)
            
            #user_information = Account()
        # if registerform.errors != {}:
        #     for err_msg in registerform.errors.values():
        #         print(f"Houve um erro ao criar a conta: {err_msg[0]}")
        #         print(type(err_msg))
        
    return render_template("register.html", form = registerform)

def role_required(role):
    def decorator(f):
        @login_required
        def decorated_function(*args, **kwargs):
            if Employees.role != role:
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator