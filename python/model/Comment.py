"""
@author:金龙
@school:hrbust
@depart:computer
@file: Comment.py
@time: 2017/12/26 21:03
@describe:评论回复
"""
from web import db
from sqlalchemy.sql import func
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    topic_id = db.Column(db.INTEGER, db.ForeignKey('topic.id'), nullable=False)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'), nullable=False)
    resume_id = db.Column(db.INTEGER, db.ForeignKey('resume.id'), nullable=True)
    on_date = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    context = db.Column(db.TEXT)

    def __init__(self, topic_id, user_id, resume_id=None, on_date=datetime.now(), context=''):
        self.topic_id = topic_id
        self.user_id = user_id
        self.resume_id = resume_id
        self.on_date = on_date
        self.context = context

    def __repr__(self):
        return "<Comment id:%d, topic_id:%d, resume_id:%d, on_date:%s>" % (
            self.id, self.topic_id, self.resume_id, self.on_date)
