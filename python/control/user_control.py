"""
@author:金龙
@school:hrbust
@depart:computer
@file: user_control.py
@time: 2017/12/26 18:47
@describe:
"""
from web import app
from flask import render_template
from python.model.User import User


@app.route('/login')
def user_index():
    return render_template('index.html')
