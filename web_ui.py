from poebot import Poebot
from bottle import run, route, request, template, static_file
import json

poe = Poebot('log.html')

@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, root='/home/pi/poebot/static')

@route('/speak', method='POST')
def speak():
    post_data = json.load(request.body)
    user_color = poe.talk(post_data['message'], request.remote_addr)
    return user_color


@route('/')
def index():
    return template('index')

run(host='192.168.1.222', port=8080)
