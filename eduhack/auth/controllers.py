from flask import Blueprint, render_template, request, redirect, session, flash
from eduhack.auth.forms import RegisterForm, LogInForm
from eduhack.auth.models import db, User
from flask_login import login_user

auth = Blueprint(__name__, 'auth', url_prefix='/accounts')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User(email=form.email.data, first_name= form.first_name.data, last_name=form.last_name.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User created')
        return redirect('/')
    context = {
        'form': form
    }
    print(form.errors)
    return render_template('auth/register.html', **context)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    # if request.method == 'POST' and form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and user.check_password(form.password.data):
    #         login_user(user)
    #         flash('Logged in successfully.')
    #         return redirect('/dashboard')
    #     else:
    #         flash('User not found')
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.email.data == 'admin':
            return redirect('/dashboard')
        if form.email.data == 'teacher':
            return redirect('/teacher/main')
        if form.email.data == 'student':
            return redirect('/student')

    return render_template('auth/login.html', **context)



@auth.route('/profile', methods=['GET', 'POST',])
def profile():
    return render_template('auth/profile.html')