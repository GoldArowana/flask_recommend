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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index2/')
def index2():
    return render_template('base.html')


@app.route('/news/')
def news():
    return render_template('news.html')


@app.route('/grid/')
def grid():
    return render_template('grid.html')


@app.route('/charts/')
def charts():
    return render_template('charts.html')


@app.route('/account/')
def account():
    return render_template('account.html')


@app.route('/vip/')
def vip():
    return render_template('vip.html')


@app.route('/login/')
def login():
    return render_template('login.html')
