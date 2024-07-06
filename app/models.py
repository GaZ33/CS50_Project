from app import db
from flask_login import UserMixin

"""
Criando as tabelas do nosso banco de dados
"""
class Account(db.model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=30), nullable=False, unique=True)
    Password = db.Column(db.String(length=80))
    

class Information(db.model, UserMixin):
    Id = db.column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=30), nullable=False)
    City = db.Column(db.String(length=20))
    Street = db.Column(db.String(length=30))
    Neighborhood = db.Column(db.String(length=30))
    Category = db.Column(db.String(length=3), nullable=False)
    Cellphone = db.column(db.String(length=16))
    #Birthday = 
    # Criando A relação de 1 para 1 no banco de dados
    Account_id = db.Column(db.integer(), db.ForeignKey('Account.Id'))