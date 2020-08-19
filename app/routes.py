from app import app
from flask import render_template

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
        }

    ]
    return render_template('index.html', title='Home', user = user, posts=posts)