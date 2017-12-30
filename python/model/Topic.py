"""
@author:金龙
@school:hrbust
@depart:computer
@file: Content.py
@time: 2017/12/26 21:03
@describe:主题
"""
from web import db
from sqlalchemy.sql import func
from datetime import datetime


class Topic(db.Model):
    __tablename__ = 'topic'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    on_datetime = db.Column(db.DateTime, server_default=func.now())
    context = db.Column(db.TEXT)
    title = db.Column(db.VARCHAR(100))
    tag = db.Column(db.VARCHAR(255))

    def __init__(self, company_id, user_id, on_datetime=datetime.now(), title='', tag='', context=''):
        self.company_id = company_id
        self.user_id = user_id
        self.on_datetime = on_datetime
        self.context = context
        self.title = title
        self.tag = tag

    def __repr__(self):
        return "<Topic id:%d, company_id:%d, user_id:%d, on_datetime:%s, context:%s, title:%s, tag:%s>" % (
            self.id, self.company_id, self.user_id, self.on_datetime, self.context, self.title, self.tag)
