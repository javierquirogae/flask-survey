from flask import Flask, request, render_template,  redirect, flash,  jsonify, session
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

MOVIES = {'Amadeus', 'Chicken Run', 'Dances With Wolves'}

@app.route('/')
def start_page():
    """Shows start"""
    return render_template('start.html')

@app.route('/question_1')
def question_1_page():
    """Shows question 1t"""
    name = request.args['name']
    question = surveys[name].questions[0].question
    return render_template('question_1.html',title=name, question=question)