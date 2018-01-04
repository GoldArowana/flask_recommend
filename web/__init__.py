"""
@author:金龙
@school:hrbust
@depart:computer
@file: __init__.py.py
@time: 2017/12/26 18:43
@describe:
"""
from flask import Flask, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import logging
import time
import functools

app = Flask(__name__)  # type:Flask

# 让jinja支持break continue语句
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# 导入配置文件
app.config.from_pyfile('app.conf')

app.secret_key = 'king'


def log(level, msg):
    log_level = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if log_level.get(level) is not None:
        app.logger.log(log_level[level], "[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "] " + msg)
    return 'logged:' + msg


def login_require(func):
    @functools.wraps(func)
    def wrapper():
        if session.get('username') is not None:
            print('not null')
            return func()
        else:
            return redirect('/login/')

    return wrapper

db = SQLAlchemy(app)

# 导入control层
from python import control
from python import model
