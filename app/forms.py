from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


"""
Criando formulários para recuperar os dados colocados pelo usuário
"""
class LoginForm(FlaskForm):
     Username = StringField(label="Username", validators=[Length(min=5, max=15), DataRequired()])
     Password = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
     Submit = SubmitField(label="Sign in")


class RegisterForm(FlaskForm):
    Username = StringField(label="Username*", validators=[Length(min=5, max=15), DataRequired()])
    Email = EmailField(label="Email*", validators=[Email(),Length(max=50)])
    FName = StringField(label="First name*", validators=[Length(max=20), DataRequired()])
    MName = StringField(label="Midle name", validators=[Length(max=20)])
    LName = StringField(label="Last name*", validators=[Length(max=20), DataRequired()])
    Category = StringField(label="Category*", validators=[Length(max=3), DataRequired()])
    Password1 = PasswordField(label="Passowrd*", validators=[Length(min=6), DataRequired()])
    Password2 = PasswordField(label="Confirm password*", validators=[EqualTo("Password1"), DataRequired()])
    Submit = SubmitField(label="Submit")
