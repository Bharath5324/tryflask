from app import app
from flask import render_template
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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('forms.html', form = form, title="Sign In")