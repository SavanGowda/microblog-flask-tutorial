from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    #return "Hello World! from Savan"

    user = {'username' : 'Viewers'}

    posts = [
        {
            'author': {'username':'Jon'},
            'body': 'I am the Commander of the Nightswatch!'
        },

        {
            'author': {'username':'Nedd'},
            'body': 'One who passes the sentence, must swing the sword!'
        },

        {
            'author': {'username':'Ygritte'},
            'body': 'You know nothing Jon Snow!'
        },

        {
            'author': {'username':'Cersi'},
            'body': 'The Iron throne is mine and I shall keep it!'
        }
    ]

    return render_template('index.html', title = 'Home', user=user, posts = posts)

@app.route('/login' , methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)
