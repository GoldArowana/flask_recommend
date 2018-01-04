"""
@author:金龙
@school:hrbust
@depart:computer
@file: index.py
@time: 2017/12/28 13:01
@describe:
"""
from web import app, log, login_require
from flask import render_template, jsonify, request


@app.route('/', methods={'get', 'post'})
def index():
    return render_template('index.html')


@app.route('/charts/', methods={'get', 'post'})
@login_require
def charts():
    return render_template('charts.html')


@app.route('/account/', methods={'get', 'post'})
@login_require
def account():
    print('123')
    return render_template('account.html')


@app.route('/settings/', methods={'get', 'post'})
@login_require
def settings():
    return render_template('settings.html')


@app.route('/vip/', methods={'get', 'post'})
@login_require
def vip():
    return render_template('vip.html')


@app.route('/login/', methods={'get', 'post'})
def login():
    return render_template('login.html')


@app.route('/register/', methods={'get', 'post'})
def register():
    return render_template('register.html')


@app.errorhandler(404)
def error_404(error):
    log("error", "<404> path:" + str(request.path))
    return render_template("flappy_bird.html"), 404
