from poebot import Poebot
from bottle import run, route, request, template, static_file
from config import Config
import json

cfg = Config('poebot.cfg')

poe = Poebot(cfg.log_file)
poe.set_command(cfg.speech_command)

@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, root=cfg.static_dir)

@route('/speak', method='POST')
def speak():
    post_data = json.load(request.body)
    if 'new_color' in post_data:
        new_color = True
    else:
        new_color = False
    user_color = poe.talk(post_data['message'], request.remote_addr, new_color=new_color)
    return user_color

@route('/about')
def about():
    return template('about')

@route('/')
def index():
    return template('index')

run(host=cfg.addr, port=cfg.port)
