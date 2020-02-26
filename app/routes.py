from flask import render_template
from app import app

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
