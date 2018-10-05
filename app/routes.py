from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from random import randint

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Andres'}
    posts =[
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'
        .format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/random')
def rand():
    r = randint(0, 10)
    return render_template('random.html', r=str(r))
