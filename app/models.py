from app import db
from flask_login import UserMixin

"""
Criando as tabelas do nosso banco de dados
"""
class Account(db.model, UserMixin):
    IdUsers = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=25), nullable=False, unique=True)
    Password = db.Column(db.String(length=80))
    

class Information(db.model, UserMixin):
    IdInformation = db.column(db.Integer(), primary_key=True)
    FName = db.Column(db.String(length=20), nullable=False)
    MName = db.Column(db.String(length=40))
    LName = db.Column(db.String(length=30), nullable=False)
    Email = db.Column(db.String(length=50))
    City = db.Column(db.String(length=20))
    Street = db.Column(db.String(length=30))
    Neighborhood = db.Column(db.String(length=30))
    Category = db.Column(db.String(length=3), nullable=False)
    Cellphone = db.column(db.String(length=16))
    Birthday = db.Column(db.Date())
    # Criando A relação de 1 para 1 no banco de dados
    Account_id = db.Column(db.integer(), db.ForeignKey('Account.Id'))