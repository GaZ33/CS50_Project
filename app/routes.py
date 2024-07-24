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
    choice = ChoiceInstructor()
    query_instructor = Employees.query.filter_by(Role="Instructor")
    choice.Instructor.choices = [(instructor.Id, instructor.FName) for instructor in query_instructor]
    if request.method == "POST":

        if choice.validate_on_submit:
            try:
                dia = str(request.form["dia"])
                hora = int(request.form["hora"])
                employee_id = request.form["employee_id"]
                if dia != "None":
                    new_day = int(dia[-2:])
                    new_month = int(dia[-5:-3])
                    new_year = int(dia[0:4])
                    # FAZER A LÓGICA DE UPDATE NO DB AQ
                    new_date = datetime(year=new_year, month=new_month, day=new_day, hour=hora)
                    # FAZER A LÓGICA DE UPDATE NO DB AQ
                    new_class = Classes(Date=new_date, Account_id=current_user.Id, Employees_id=employee_id)
                    db.session.add(new_class)
                    db.session.commit()
                    print(new_date)
                    #new_class = Classes(date)
                    
                return redirect(url_for('index'))

            except:
                print()
            


            today = datetime.today()
            # jé vem o ID ao invés do nome
            employee_choosed = choice.Instructor.data
            day1 = timedelta(days=1)
            #nova_classe = Classes(Date = today, Account_id=current_user.Id, Employees_id=employee_choosed)
            #db.session.add(nova_classe)
            #db.session.commit()
            employee_scheduale = Classes.query.filter(and_(Classes.Employees_id==employee_choosed, func.date(Classes.Date)==today.date())).all()
            week = dict()
            for day in range(0,7):
                if today.weekday() == 6:
                    today = today+day1
                    continue
                
                date = (today.date())
                week[date] = dict()
                employee_scheduale = Classes.query.filter(and_(Classes.Employees_id==employee_choosed, func.date(Classes.Date)==today.date())).all()
                for hora in employee_scheduale:
                    week[date][hora.Date.hour] = True
                for j in range(5,24):
                    if j in week[date]:
                        continue
                    if j == 12:
                        continue
                    week[date][j] = False
                today = today+day1
                week[date] = sorted(week[date].items()) 
            #print(week)
            return render_template("scheduale.html", form=choice, week=week, employee_id=employee_choosed)
        
        else:
            week = dict()
            flash("Problema com o instrutor", category="Danger")
            render_template("scheduale.html", form=choice, week=week, employee_id=None)
        
        

    week = dict()
    return render_template("scheduale.html", form=choice, week=week, employee_id=None)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


