from app import db, login_manager
from flask_login import UserMixin
from app import Bcrypt

"""
Criando as tabelas do nosso banco de dados
"""
class Account(db.Model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=25), nullable=False, unique=True)
    Password = db.Column(db.String(length=80), nullable=False)
    @property
    def password(self):
        return self.Password
    
    @password.setter
    def password_hash(self, Password):
        self.Password = Bcrypt.generate_password_hash(Password).decode('utf-8')

    def check_password(self, attempted_password):
        return Bcrypt.check_password_hash(self.Password, attempted_password)
    
    def get_id(self):
        return int(self.Id)
    # Dizendo ao modelo sobre as relações
    informations = db.relationship('Information', backref='Account', lazy=True)
    performance = db.relationship('Performance', backref='Performance', lazy=True)
    classes = db.relationship('Classes', backref='Classes', lazy=True)
    

class Information(db.Model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    FName = db.Column(db.String(length=20), nullable=False)
    MName = db.Column(db.String(length=40))
    LName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50))
    City = db.Column(db.String(length=20))
    Street = db.Column(db.String(length=30))
    Neighborhood = db.Column(db.String(length=30))
    Category = db.Column(db.String(length=3), nullable=False)
    Cellphone = db.column(db.String(length=16))
    Birthday = db.Column(db.DateTime())
    # Criando A relação de 1 para 1 no banco de dados
    Account_id = db.Column(db.Integer, db.ForeignKey('account.Id'), nullable=False)
    #account = db.relationship('Account', backref=db.backref('information', uselist=False), lazy=True)

class Employees(db.Model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=25), nullable=False)
    Password = db.Column(db.String(length=80), nullable=False)
    FName = db.Column(db.String(length=20), nullable=False)
    MName = db.Column(db.String(length=40))
    LName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50))
    Cellphone = db.column(db.String(length=16))
    Birthday = db.Column(db.DateTime())
    def get_id(self):
        return int(self.Id)
    
    @property
    def Password(self):
        return self.Password
    
    @Password.setter
    def password_hash(self, password):
        self.password = Bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, attempted_password):
        return Bcrypt.check_password_hash(self.Password, attempted_password)
    performance = db.relationship('Performance', backref='Performance', lazy=True)
    classes = db.relationship('Classes', backref='Classes', lazy=True)

class Performance(db.Model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    Driving = db.Column(db.Float(), nullable=False)
    Parking = db.Column(db.Float(), nullable=False)
    Parallel_parking = db.Column(db.Float(), nullable=False)
    Attention = db.Column(db.Float(), nullable=False)
    # Relações
    Account_id = db.Column(db.Integer, db.ForeignKey('account.Id'), nullable=False)
    Employees_id = db.Column(db.Integer, db.ForeignKey('employees.Id'), nullable=False)

class Classes(db.Model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    Date = db.Column(db.DateTime())
    Account_id = db.Column(db.Integer, db.ForeignKey('account.Id'), nullable=False)
    Employees_id = db.Column(db.Integer, db.ForeignKey('employees.Id'), nullable=False)
    # Relações
    Account_id = db.Column(db.Integer, db.ForeignKey('account.Id'), nullable=False)
    Employees_id = db.Column(db.Integer, db.ForeignKey('employees.Id'), nullable=False)

@login_manager.user_loader
def load_user(user):
    user_type, id = user.split(":")

    if user_type == "account":
        return Account.query.get(id)
    elif user_type == "employee":
        return Employees.query.get(id)
    else:
        return None