from email import message
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import *
from ..models import *

class RegistrationForm(FlaskForm):
    email=StringField('Email Address',validators=[InputRequired(),Email()],render_kw={"placeholder": "janedoe@example.com"})
    username=StringField('Username',validators=[InputRequired()],render_kw={"placeholder":"janedoe"})
    password=PasswordField('Password',validators=[InputRequired(),EqualTo('password_confirm',message='Passwords do not match')],render_kw={"placeholder":"********"})
    password_confirm=PasswordField('Confirm Password',validators=[InputRequired()],render_kw={"placeholder":"********"})
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('An account has already been registered with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('Username already exists.')

class SigninForm(FlaskForm):
    email=StringField('Email Address',validators=[InputRequired(),Email()],render_kw={"placeholder": "janedoe@example.com"})
    password=PasswordField('Password',validators=[InputRequired()],render_kw={"placeholder":"********"})
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')