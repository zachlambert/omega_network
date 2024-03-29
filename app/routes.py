from flask import render_template, jsonify, request, url_for

from app import app
from app import db
from app.models import Agent

from app.errors import bad_request
from app.agents import new_agent
from app.info import get_info
from app.processing import process_speech, process_image

# GET requests should only return information, making no changes
# POST requests are used for requests which cause changes
# The speech and image endpoints are POST because although their primary
# usage is to process something and return a response, this may in future
# include updating information contained in the brain.

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/new', methods=['POST'])
def new():
    agent = new_agent()
    response = jsonify(agent.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('get_agent', id=agent.id)
    return response

@app.route('/agent/<int:id>', methods=['GET'])
def get_agent(id):
    return(Agent.query.get_or_404(id).to_dict())

@app.route('/info/<string>', methods=['GET'])
def info(string):
    results = get_info(string)
    response = jsonify(results)
    response.status_code = 201
    return reponse

@app.route('/speech', methods=['POST'])
def speech():
    data = request.files['file'] or None 
    if data is None:
        return bad_request('must include sound file')
    results = process_speech(data)
    response = jsonify(results)
    response.status_code = 201
    return response

@app.route('/image', methods=['POST'])
def image():
    data = request.files['file'] or None
    if data is None:
        return bad_request('must include image')
    results = process_image(data)
    response = jsonify(results)
    response.status_code = 201
    return response

@app.cli.command('resetdb')
def resetdb_command():
    print('Dropping tables')
    db.drop_all()
    print('Creating tables')
    db.create_all()
    db.drop_all()
    db.create_all()
