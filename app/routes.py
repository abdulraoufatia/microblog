from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Abdulraouf Atia'}
    posts = [
        {
            'author': {'username': 'Abdulraouf'},
            'body': 'Beautiful day in London, UK!'
        },
        {
            'author': {'username': 'Abdulraouf'},
            'body': 'The Adams Project movie was great'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run()
