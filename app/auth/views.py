from . import auth
from flask import render_template,redirect,url_for,request,flash
from ..models import *
from .forms import *
from .. import db
from flask_login import *
from ..email import mail_message


@auth.route('/signup',methods=['GET','POST'])
def signup():
    signup_form = RegistrationForm()
    if signup_form.validate_on_submit():
        user = User(email=signup_form.email.data, username=signup_form.username.data, password=signup_form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Pitch-Me","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    title="SignUp"
    return render_template('auth/signup.html',signup_form=signup_form, title=title)

@auth.route('/signin',methods=['GET','POST'])
def login():
    signin_form = SigninForm()
    if signin_form.validate_on_submit():
        user = User.query.filter_by(email = signin_form.email.data).first()
        if user is not None and user.verify_password(signin_form.password.data):
            login_user(user,signin_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "SignIn"
    return render_template('auth/signin.html',signin_form = signin_form,title=title)

@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for("main.index"))