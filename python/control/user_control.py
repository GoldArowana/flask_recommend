"""
@author:金龙
@school:hrbust
@depart:computer
@file: user_control.py
@time: 2017/12/26 18:47
@describe:
"""
from web import app, db
from flask import render_template, request, redirect, flash, session, jsonify
from python.model.User import User  # type:User
from sqlalchemy.sql import func


@app.route('/login_check/', methods={'get', 'post'})
def login_check():
    username = request.values.get('username')
    password = request.values.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        flash('登陆失败')
        return redirect('/login/')
    else:
        session['username'] = username
        # print(session['username'])
        return redirect('/')


@app.route('/logout/', methods={'get', 'post'})
def logout():
    session.pop('username')
    return redirect('/')


@app.route('/get_user_count/', methods={'get', 'post'})
def get_user_count():
    user_count = db.session.query(func.count('*')).select_from(User).scalar()
    return jsonify(user_count)
