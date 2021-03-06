"""
@author:金龙
@school:hrbust
@depart:computer
@file: User.py
@time: 2017/12/26 19:13
@describe:用户
"""
from web import db
from random import randint
from datetime import date


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    salt = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    sex = db.Column(db.Enum('o', 'm', 'f'))
    graduate_year = db.Column(db.SmallInteger)
    name = db.Column(db.String(20), nullable=True)
    topics = db.relationship("Topic", backref='user')
    comments = db.relationship("Comment", backref='user')
    resumes = db.relationship("Resume", backref='user')
    email = db.relationship("Email", backref='user', uselist=False)
    vip = db.relationship("Vip", backref='user', uselist=False)

    def __init__(self, username, password, salt='', head_url='', sex='o', graduate_year=int(date.today().year),
                 name=''):
        self.username = username
        self.password = password
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(randint(0, 1000)) + 'm.png'
        self.sex = sex
        self.graduate_year = graduate_year
        self.name = name

    def __repr__(self):
        return "<User id:%d, username:%s, password:%s, salt:%s, head:%s, sex:%s,graduate_year:%s>" % (
            self.id, self.username, self.password, self.salt, self.head_url, self.sex, self.graduate_year)
