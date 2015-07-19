from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import FloatField
from wtforms import PasswordField
from wtforms.validators import DataRequired
from wtforms.validators import Email


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(Form):
    email = StringField('email', validators=[DataRequired(), Email('Valid email required')])
    password = PasswordField('password', validators=[DataRequired()])


class GuessForm(Form):
    gender = StringField('gender')
    weight = FloatField('weight', validators=[DataRequired()])
    eyes = StringField('eyecolor', validators=[DataRequired()])
    hair = StringField('haircolor', validators=[DataRequired()])
    length = FloatField('bodylength', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
