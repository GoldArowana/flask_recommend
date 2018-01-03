"""
@author:金龙
@school:hrbust
@depart:computer
@file: Email.py
@time: 2018/1/3 12:48
@describe:
"""
from web import db


class Email(db.Model):
    __tablename__ = 'email'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'))
    email_address = db.Column(db.String(255), nullable=False)
    email_checked = db.Column(db.SmallInteger, server_default='0')

    def __init__(self, user_id, email_address='', email_checked=0):
        user_id = user_id
        email_address = email_address
        email_checked = email_checked

    def __repr__(self):
        return "<Email: id:%d, user_id:%d, email_address:%s, email_checked:%d>" % (
            self.id, self.user_id, self.email_address, self.email_checked)
