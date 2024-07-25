from app import render_template, redirect, url_for, request, session, datetime, timedelta, and_, func, date
from app import app, login_user, login_required, flash, logout_user, current_user
from app.models import Account, Information, Employees, db, Classes, Performance
from app.forms import LoginForm, RegisterForm, ProfileForm, ChoiceInstructor



# Função para restringir usuários de certas páginas
# É necessário colocar ela aqui em cima
def role_required(role):
    def decorator(f):
        @login_required
        def decorated_function(*args, **kwargs):
            if Employees.role != role:
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
""" 
Criando rotas para páginas do site 
"""

# Index.html
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

# Login.html
@app.route("/login", methods=['GET', 'POST'])
def login():
    # Chamando a instância de formulário para a página
    loginform = LoginForm()
    # Executando a tentativa de login quando o forms for enviado
    if request.method == "POST":
        # Validando o formulário
        if loginform.validate_on_submit():
            # Buscando os resultados no database
            attempted_user = Account.query.filter_by(Username=loginform.Username.data).first()
            # Verificando se houve uma instância e se a senha match
            if attempted_user and attempted_user.check_password(loginform.Password.data):
                # Fazendo o login do usuário
                session['user_type'] = 'account'
                login_user(attempted_user)
                return redirect(url_for("scheduale"))
            else:
                flash("Username and password doesn't match", category="danger")
                
    return render_template("login.html", form = loginform)

# Login_employees.html
@app.route("/loginemployees", methods=["GET", "POST"])
def login_employees():
    # Chamando a instância de formulário para a página
    loginform = LoginForm()
    # Executando a tentativa de login quando o forms for enviado
    if request.method == "POST":
        # Validando o formulário
        if loginform.validate_on_submit():
            # Buscando os resultados no database
            attempted_user = Employees.query.filter_by(Username=loginform.Username.data).first()
            # Verificando se houve uma instância e se a senha match
            if attempted_user and attempted_user.check_password(loginform.Password.data):
                # Fazendo o login do usuário
                session['user_type'] = 'employee'
                login_user(attempted_user)
                return redirect(url_for("schedualeemployee"))
                
    return render_template("loginemployee.html", form = loginform)

@app.route("/schedualeemployee", methods=["GET", "POST"])
def schedualeemployee():
    # Requisitando a data de hoje para exibir
    today = datetime.today()

    # Colocando o dia como 1, para somar e assim usar essa variável para os demais dias
    day1 = timedelta(days=1)

    week = dict()
    # Primeiro for: Iterar sobre os 6 dias
    for day in range(0,7):
        # If para pular o domingo
        if today.weekday() == 6:
            today = today+day1
            continue
        # Criando a data do dia
        # OBS: Esse today é uma variável que vai trocando os dias
        date = (today.date())
        week[date] = dict()
        # Query para encontrar os agendamentos do funcionário no dia

        employee_scheduale = Classes.query.filter(and_(Classes.Employees_id==current_user.Id, func.date(Classes.Date)==today.date())).all()

        # Colocando os agendamentos do funcionário no dicionário
        for hora in employee_scheduale:
            if hora.Account_id == 2:
                week[date][hora.Date.hour] = [True, 2]
            else:
                week[date][hora.Date.hour] = [True, 1]
        # Preenchendo as demais aulas que não foram marcadas
        for j in range(5,24):
            # Se já tiver com algum horário preenchido, pule
            if j in week[date]:
                continue
            # Horário de almoço
            if j == 12:
                continue
            week[date][j] = [False, None]
        # Aqui fazemos a troca do dia, passa de segunda para terça, terça para quarta ...
        today = today+day1
        # Organizando os itens para não ficarem com um display errado no html
        week[date] = sorted(week[date].items()) 


    if request.method == "POST":
            print(current_user.Id)
            dia = str(request.form["dia"])
            hora = int(request.form["hora"])
            delete = str(request.form["delete"])

            new_day = int(dia[-2:])
            new_month = int(dia[-5:-3])
            new_year = int(dia[0:4])
            if delete == "False":
                # realizar query para colcoar o id do user = a 0
                date_to_free = datetime(year=new_year, 
                                        month=new_month, 
                                        day=new_day, 
                                        hour=hora)
                new_free_time = Classes(Date=date_to_free, 
                                        Employees_id=current_user.Id, 
                                        Account_id=2)
                db.session.add(new_free_time)
                db.session.commit()
                return redirect(url_for('schedualeemployee'))
            else:
                # Deletar o dia que pode ser free time ou algum cliente
                # Criando a data para excluir a folga ou a classe
                date_to_delete = datetime(year=new_year, 
                                        month=new_month, 
                                        day=new_day, 
                                        hour=hora)
                # Query para procurar a informação no DB
                query_to_delete = Classes.query.filter(and_(Classes.Employees_id==current_user.Id, 
                                                            Classes.Account_id==current_user.Id, 
                                                            Classes.Date==date_to_delete)).first()
                db.session.delete(query_to_delete)
                db.session.commit()
                return redirect(url_for('schedualeemployee'))
                
    return render_template("schedualeemployee.html", week = week)



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
                                  Password_text=registerform.Password1.data)
            # Verificando se não há usuários com o mesmo nome
            query_check_user = Account.query.filter_by(Username=user_create.Username).first()
            if registerform.errors != {}:
                for err_msg in registerform.errors.values():
                     flash(f"Houve um erro ao criar a conta: {err_msg[0]}")
            if query_check_user:
                flash(message="Já existe um usuário com esse Username", category="danger")
            
            else:
                # Adicionando a instância no database
                db.session.add(user_create)
                # Enviando as mudanças
                db.session.commit()
                query_information = Account.query.filter_by(Username=user_create.Username).first()
                information = Information(FName=registerform.FName.data, 
                                          MName=registerform.MName.data,
                                          LName=registerform.LName.data,
                                          Category=registerform.Category.data,
                                          Email=registerform.Email.data,
                                          Account_id=query_information.Id)
                db.session.add(information)
                db.session.commit()
                login_user(user_create)
                session['user_type'] = 'account'

                return redirect(url_for("scheduale"))

            
        
    return render_template("register.html", form = registerform)

@app.route("/schedualeemployee", methods=["GET", "POST"])
@role_required("employee")
def scheduale_employee():
    return render_template("schedualeemployee.html")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    query_account = Account.query.filter_by(Username=current_user.Username).first()
    query_information = Information.query.filter_by(Account_id=query_account.Id).first()
    profileform = ProfileForm(Email=query_information.Email,
                       FName=query_information.FName,
                       MName=query_information.MName,
                       LName=query_information.LName,
                       City=query_information.City,
                       Street=query_information.Street,
                       Neighborhood=query_information.Neighborhood,
                       Category=query_information.Category,
                       Cellphone=query_information.Cellphone,
                       Birthday=query_information.Birthday)
    if request.method == "POST":
        if profileform.validate_on_submit:
            query_information.Email = profileform.Email.data
            query_information.FName = profileform.FName.data
            query_information.MName = profileform.MName.data
            query_information.City = profileform.City.data
            query_information.Street = profileform.Street.data
            query_information.Neighborhood = profileform.Neighborhood.data
            query_information.Category = profileform.Category.data
            query_information.Cellphone = profileform.Cellphone.data
            query_information.Birthday = profileform.Birthday.data
            db.session.commit()
            return redirect("scheduale")
    return render_template("profile.html", form=profileform)

@app.route("/scheduale", methods=["GET", "POST"])
@login_required
def scheduale():
    # Form para escolha de instrutor
    choice = ChoiceInstructor()
    # Query para ver quais instrutores existem
    query_instructor = Employees.query.filter_by(Role="Instructor")
    # Colocando as possibilidades no forms
    choice.Instructor.choices = [(instructor.Id, instructor.FName) for instructor in query_instructor]

    if request.method == "POST":
        # Se o forms for validado
        if choice.validate_on_submit:
            """
            No primeiro submit, não haverá o dia, então o try pulará
            """
            # Quando o usuário clicar em algum horário executará o try
            # FUTURE_UPDATE: tentar trocar esse try por um if dia != "None"
            try:
                # FUTURE_UPDATE: remover o request de dia e colocar o if
                # Fazendo os request necessários para a alateração
                delete = str(request.form["delete"])
                dia = str(request.form["dia"])
                hora = int(request.form["hora"])
                employee_id = request.form["employee_id"]

                # If que executará a deleção do appointment
                if delete == "True":
                    # Separando o dia, mes e ano do formato que vêm
                    # Formato: YYYY/MM/DD
                    new_day = int(dia[-2:])
                    new_month = int(dia[-5:-3])
                    new_year = int(dia[0:4])
                    # Criando a data para excluir o appointment
                    date_to_delete = datetime(year=new_year, 
                                              month=new_month, 
                                              day=new_day, 
                                              hour=hora)
                    # Query para procurar a informação no DB
                    query_to_delete = Classes.query.filter(and_(Classes.Employees_id==employee_id, 
                                                                Classes.Account_id==current_user.Id, 
                                                                Classes.Date==date_to_delete)).first()
                    # Deletando a instância
                    db.session.delete(query_to_delete)
                    db.session.commit()
                    return redirect(url_for('index'))

                """
                No primeiro submit, não haverá o dia, então o dia vem como None
                """
                if dia != "None":
                    # Fazendo os request necessários para a alateração
                    new_day = int(dia[-2:])
                    new_month = int(dia[-5:-3])
                    new_year = int(dia[0:4])
                    # Criando a data para adicionar o appointment
                    new_date = datetime(year=new_year, 
                                        month=new_month, 
                                        day=new_day, 
                                        hour=hora)
                    # Query para procurar a informação no DB
                    new_class = Classes(Date=new_date, 
                                        Account_id=current_user.Id, 
                                        Employees_id=employee_id)
                    # Adicionando a informação no DB
                    db.session.add(new_class)
                    db.session.commit()
                    return redirect(url_for('index'))

            except:
                # Única maneira que achei para evitar erros
                print()
            

            # Requisitando a data de hoje para exibir
            today = datetime.today()
            # Request do forms choice
            # jé vem o ID ao invés do nome
            employee_choosed = choice.Instructor.data
            # Colocando o dia como 1, para somar e assim usar essa variável para os demais dias
            day1 = timedelta(days=1)
            # Fazendo a query do dia de hoje com aquele funcionário
            #
            #
            # Excluir??
            employee_scheduale = Classes.query.filter(and_(Classes.Employees_id==employee_choosed, func.date(Classes.Date)==today.date())).all()
            week = dict()
            # Primeiro for: Iterar sobre os 6 dias
            for day in range(0,7):
                # If para pular o domingo
                if today.weekday() == 6:
                    today = today+day1
                    continue
                # Criando a data do dia
                # OBS: Esse today é uma variável que vai trocando os dias
                date = (today.date())
                week[date] = dict()
                # Query para encontrar os agendamentos do funcionário no dia
                employee_scheduale = Classes.query.filter(and_(Classes.Employees_id==employee_choosed, func.date(Classes.Date)==today.date())).all()
                # Query para encontrar algum agendamento do cliente para aquele funcionário
                user_scheduale = Classes.query.filter(and_(Classes.Account_id==current_user.Id, 
                                                        Classes.Employees_id==employee_choosed,
                                                        func.date(Classes.Date)==today.date())).all()
                # Colocando os agendamentos do funcionário no dicionário
                for hora in employee_scheduale:
                    week[date][hora.Date.hour] = [True, None]

                """
                Colocando os agendamentos do cliente no dicionário
                Vai sobre-escrever nos horários do for de cima, caso o cliente já tenha horário marcado
                É necessário esse for para que o cliente possa apgar as aulas dele
                """
                for hora in user_scheduale:
                    week[date][hora.Date.hour] = [True, int(current_user.Id)]
                # Preenchendo as demais aulas que não foram marcadas
                for j in range(5,24):
                    # Se já tiver com algum horário preenchido, pule
                    if j in week[date]:
                        continue
                    # Horário de almoço
                    if j == 12:
                        continue
                    week[date][j] = [False, None]
                # Aqui fazemos a troca do dia, passa de segunda para terça, terça para quarta ...
                today = today+day1
                # Organizando os itens para não ficarem com um display errado no html
                week[date] = sorted(week[date].items()) 
            return render_template("scheduale.html", form=choice, week=week, employee_id=employee_choosed)
        # Problema ao requisitar o instrutor
        else:
            # Criando um dicionário vázio para renderizar a página novamente
            week = dict()
            flash("Problema com o instrutor", category="danger")
            render_template("scheduale.html", form=choice, week=week, employee_id=None)
        
        
    # Criando um dicionário vázio para renderizar a página
    week = dict()
    return render_template("scheduale.html", form=choice, week=week, employee_id=None)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


