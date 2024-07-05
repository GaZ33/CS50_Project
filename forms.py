from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError



class LoginForm(FlaskForm):
     Username = StringField(label="Username", validators=[Length(min=5, max=15), DataRequired()])
     Password = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
     Submit = SubmitField(label="Submit")


class RegisterForm(FlaskForm):
    Username = StringField(label="username", validators=[Length(min=5, max=15), DataRequired()])
    Password1 = PasswordField(label="Passowrd", validators=[Length(min=6), DataRequired()])
    Password2 = PasswordField(label="Confirm password", validators=[EqualTo("password1"), DataRequired()])
    Submit = SubmitField(label="Submit")