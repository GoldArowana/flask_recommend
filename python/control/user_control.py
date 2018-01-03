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


@app.route('/add_user/', methods={'get', 'post'})
def add_user():
    username = request.values.get('username')
    password = request.values.get('password')
    sex = request.values.get('sex')
    graduate_year = request.values.get('graduate_year')
    netname = request.values.get('netname')
    email_address = request.values.get('email_address')
    flash('您已注册成功, 请登录')
    return redirect('/login/')


@app.route('/username_check/', methods={'post'})
def username_check():
    username = request.values.get('username')
    print(username)
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'has_username': False})
    else:
        return jsonify({'has_username': True})
