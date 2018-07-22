from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in West Yorkshire!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so uncool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

