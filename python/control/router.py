"""
@author:金龙
@school:hrbust
@depart:computer
@file: index.py
@time: 2017/12/28 13:01
@describe:
"""
from web import app
from flask import render_template


@app.route('/', methods={'get', 'post'})
def index():
    return render_template('index.html')


@app.route('/index2/', methods={'get', 'post'})
def index2():
    return render_template('base.html')


@app.route('/grid/', methods={'get', 'post'})
def grid():
    return render_template('grid.html')


@app.route('/charts/', methods={'get', 'post'})
def charts():
    return render_template('charts.html')


@app.route('/account/', methods={'get', 'post'})
def account():
    return render_template('account.html')


@app.route('/settings/', methods={'get', 'post'})
def settings():
    return render_template('settings.html')


@app.route('/vip/', methods={'get', 'post'})
def vip():
    return render_template('vip.html')


@app.route('/login/', methods={'get', 'post'})
def login():
    return render_template('login.html')
