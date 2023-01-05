from flask import Flask, request, render_template,  redirect, flash,  jsonify, session
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

NAME = []

ANSWERS = []

@app.route('/')
def start_page():
    """Shows start"""
    return render_template('start.html')

@app.route('/survey', methods=["POST"])
def survey_choice():
    NAME.append = request.args['name']
    return redirect('/question_1')

@app.route('/question_1')
def question_1_page():
    """Shows question 1"""
    name = NAME[0]
    s = surveys[name]
    long_title = s.title
    instructions = s.instructions
    q = s.questions[0]
    question = q.question
    choices = q.choices
    return render_template('question_1.html',title=name, question=question, long_title=long_title, instructions=instructions, choices=choices)

@app.route('/question_1/answer', methods=["POST"])
def add_answer():
    ANSWERS.append = request.args['answer']
    return redirect('/question_2')

@app.route('/question_2')
def question_2_page():
    """Shows question 2"""
    s = surveys[NAME[0]]
    long_title = s.title
    instructions = s.instructions
    q = s.questions[2]
    question = q.question
    choices = q.choices
    return render_template('question_1.html',title=name, question=question, long_title=long_title, instructions=instructions, choices=choices)