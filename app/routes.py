from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from .models import User
@app.route("/")
@app.route("/index")
@login_required
def index():
    user = {'username': 'Bharath'}
    posts  = [

        {
            'author': {"username": "John"},
            'body' : 'I wanted to tweet so I tweeted'
        },
        {
            'author': {'username':'Monu'},
            'body': 'I like to tweet so I tweeted'
        },
        {
            'author': {'username':'Vava'},
            'body': 'My little berdie is all about scary stuff'
        }
    ]
    return render_template('index.html', title='Home', user = user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user, remember = form.rememberme.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author':user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post#2'}
    ]
    return render_template('user.html', user=user, posts=posts)

