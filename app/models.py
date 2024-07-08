from app import db
from flask_login import UserMixin
from app import Bcrypt

"""
Criando as tabelas do nosso banco de dados
"""
class Account(db.Model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=25), nullable=False, unique=True)
    Password = db.Column(db.String(length=80))
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password_hash(self, password):
        self.password = Bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, attempted_password):
        return Bcrypt.check_password_hash(self.Password, attempted_password)
    

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
    Account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship('Account', backref=db.backref('information', uselist=False), lazy=True)

class Employees(db.Model, UserMixin):
    IdEmployees = db.Column(db.Integer(), primary_key=True)
    FName = db.Column(db.String(length=20), nullable=False)
    MName = db.Column(db.String(length=40))
    LName = db.Column(db.String(length=30), nullable=False)