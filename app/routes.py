from app import render_template, redirect, url_for, request
from app import app, login_user, login_required, flash
from app.models import Account, Information, Employees, db
from app.forms import LoginForm, RegisterForm


""" 
Criando rotas para páginas do site 
"""

# Index.html
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

# Login.html
@app.route("/login", methods=["GET", "POST"])
def login():
    # Chamando a instância de formulário para a página
    loginform = LoginForm()
    # Executando a tentativa de login quando o forms for enviado
    if request.method == "POST":
        # Validando o formulário
        if loginform.validate_on_submit():
            # Buscando os resultados no database
            attempted_user = Account.query.filter_by(Username=loginform.Username.data)
            # Verificando se houve uma instância e se a senha match
            if attempted_user and attempted_user.check_password(loginform.Password.data):
                # Fazendo o login do usuário
                login_user(attempted_user)
    return render_template("login.html", form = loginform)

# Login_employees.html
@app.route("/login", methods=["GET", "POST"])
def login_employees():
    # Chamando a instância de formulário para a página
    loginform = LoginForm()
    # Executando a tentativa de login quando o forms for enviado
    if request.method == "POST":
        # Validando o formulário
        if loginform.validate_on_submit():
            # Buscando os resultados no database
            attempted_user = Employees.query.filter_by(Username=loginform.Username.data)
            # Verificando se houve uma instância e se a senha match
            if attempted_user and attempted_user.check_password(loginform.Password.data):
                # Fazendo o login do usuário
                login_user(attempted_user)
    return render_template("login.html", form = loginform)

@app.route("/register", methods=['GET', 'POST'])
def register():
    # Chamando a instância de formulário para a página
    registerform = RegisterForm()
    # Executando a tentativa de register quando o forms for enviado
    if request.method == 'POST':
        # Validando os inputs
        if registerform.validate_on_submit():
            # Criando uma instância de usuário
            user_create = Account(Username=registerform.Username.data,
                                  Password=registerform.Password1.data)
            # Verificando se não há usuários com o mesmo nome
            query_check_user = Account.query.filter_by(Username=user_create.Username).first()
            # TODO
            if query_check_user:
                flash(message="Já existe um usuário com esse Username", category="warmimg")
            
            else:
                # Adicionando a instância no database
                db.session.add(user_create)
                # Enviando as mudanças
                db.session.commit()
                query_information = Account.query.filter_by(Username=user_create.Username).first()
                print(query_information.Id)
                # TODO 
                # LÓGICA PARA PEGAR O ID DO USUÁIRO CRIADO E RELACIONAR COM A INFORMAÇÃO
                # Logando o usuário
                #login_user(user_create)

                #return redirect(url_for("scheduale"))



            



            #user_information = Account()
        # if registerform.errors != {}:
        #     for err_msg in registerform.errors.values():
        #         print(f"Houve um erro ao criar a conta: {err_msg[0]}")
        #         print(type(err_msg))
        
    return render_template("register.html", form = registerform)

# Função para restringir usuários de certas páginas
def role_required(role):
    def decorator(f):
        @login_required
        def decorated_function(*args, **kwargs):
            if Employees.role != role:
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator