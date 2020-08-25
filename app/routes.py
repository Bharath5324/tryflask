from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
@app.route("/")
@app.route("/index")
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
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login required for user {}, remember me = {}".format(form.username.data, form.rememberme.data))
        return redirect(url_for('index'))
    return render_template('forms.html', form = form, title="Sign In")