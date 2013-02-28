from poebot import Poebot
from bottle import run, route, request, template, static_file
from config import Config
import json

cfg = Config('poebot.cfg')

poe = Poebot(cfg.log_file)

@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, root=cfg.static_dir)

@route('/speak', method='POST')
def speak():
    post_data = json.load(request.body)
    user_color = poe.talk(post_data['message'], request.remote_addr, new_color=post_data['new_color'])
    return user_color

@route('/about')
def about():
    return template('about')

@route('/')
def index():
    return template('index')

run(host=cfg.addr, port=cfg.port)
