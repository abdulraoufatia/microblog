from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run()
