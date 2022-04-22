from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField

class SignUp(FlaskForm):
    first_name = StringField("First_name", id="first_name")
    last_name =StringField("Last name", id="last_name")
    login = StringField("Login", id="login")
    password = StringField("Password", id='password')
    gender = SelectField(u'Gender', id="gender", choices=[('male', 'Male'),
                                                          ('female', 'Female'),
                                                          ('helicopter', 'Helicopter')])
    registrer = SubmitField("Sign Up", id="form_button")


class SignIn(FlaskForm):
    login = StringField("Login", id="login")
    password = StringField("Password", id='password')
    enter = SubmitField("Sign In",  id="form_button")
    remember = BooleanField("Remember")
