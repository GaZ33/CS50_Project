from app import db
from flask_login import UserMixin
class Account(db.model, UserMixin):
    Id = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(length=30), nullable=False, unique=True)
    Password = db.Column(db.String(length=80))

