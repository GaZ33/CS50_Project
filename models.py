from app import db
from flask_login import UserMixin
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
    #Cellphone = db.column(db.String(length=))
    #Birthday = 
    Account_id = db.Column(db.integer(), db.ForeignKey('Account.Id'))