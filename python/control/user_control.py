"""
@author:金龙
@school:hrbust
@depart:computer
@file: user_control.py
@time: 2017/12/26 18:47
@describe:
"""
from web import app, db, log
from flask import request, redirect, flash, session, jsonify
from python.model import *
from sqlalchemy.sql import func
from python.control import sign_control


@app.route('/login_check/', methods={'get', 'post'})
def login_check():
    username = request.values.get('username')
    password = request.values.get('password')
    user = User.User.query.filter_by(username=username, password=password).first()
    if user is None:
        flash('登陆失败')
        log("warn", username + "login failed")
        return redirect('/login/')
    else:
        session['username'] = username
        log("info", username + " <login success>")
        # print(session['username'])
        return redirect('/')


@app.route('/logout/', methods={'get', 'post'})
def logout():
    username = session.pop('username')
    log("info", username + " <login out>")
    return redirect('/')


@app.route('/get_user_count/', methods={'get', 'post'})
def get_user_count():
    user_count = db.session.query(func.count('*')).select_from(User.User).scalar()
    return jsonify(user_count)


@app.route('/add_user/', methods={'get', 'post'})
def add_user():
    log("info", "register start**********************************************************************")
    username = request.values.get('username')
    password = request.values.get('password')
    sex = request.values.get('sex')
    graduate_year = request.values.get('graduate_year')
    netname = request.values.get('netname')
    email_address = request.values.get('email_address')
    sign_num = request.values.get('sign_email')
    log("info", "sign_num:" + sign_num)
    if not sign_control.SignHolder.sign(sign_num):
        flash('验证码错误')
        log("warn", "number signed wrong")
        log("info", "sign_list:" + str(sign_control.SignHolder.sign_list))
        log("info", "register failed**********************************************************************")
        return redirect('/register/')
    db.session.add(User.User(username, password, sex=sex, graduate_year=int(graduate_year), name=netname))
    log("info", "user inserted")
    this_user = User.User.query.filter_by(username=username).first()  # type:User
    log("info", "user orm str:" + str(this_user))
    db.session.add(Email.Email(this_user.id, email_address))
    log("info", "email information inserted")
    db.session.commit()
    flash('您已注册成功, 请登录')
    log("info", "register success**********************************************************************")
    return redirect('/login/')


@app.route('/username_check/', methods={'post'})
def username_check():
    username = request.values.get('username')
    user = User.User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'has_username': False})
    else:
        return jsonify({'has_username': True})
