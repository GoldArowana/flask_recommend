"""
@author:金龙
@school:hrbust
@depart:computer
@file: Manager.py
@time: 2017/12/26 21:02
@describe:管理员
"""

from web import db
from random import randint


class Manager(db.Model):
    __tablename__ = 'manager'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    salt = db.Column(db.String(32))
    head_url = db.Column(db.String(256), nullable=True)

    def __init__(self, username, password, salt=''):
        self.username = username
        self.password = password
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(randint(0, 1000)) + 'm.png'

    def __repr__(self):
        return "<Manager id:%d, username:%s, password:%s, salt:%s, head:%s>" % (
            self.id, self.username, self.password, self.salt, self.head_url)
