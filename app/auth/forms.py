from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField('Please enter your user-name',validators=[Required()])
    email = StringField('Email address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message='Passwords must match')])
    confirm_password = PasswordField('Confirm passwords',validators=[Required()])
    submit = SubmitField('Sign up')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('That email is taken')
    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your email address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')