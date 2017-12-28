"""
@author:金龙
@school:hrbust
@depart:computer
@file: Resume.py
@time: 2017/12/26 21:09
@describe:简历
"""

from web import db


class Resume(db.Model):
    __tablename__ = 'resume'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    path = db.Column(db.VARCHAR(255), nullable=False)
    detail = db.Column(db.VARCHAR(255))

    def __init__(self, user_id, name='简历', path='', detail=''):
        self.user_id = user_id
        self.path = path
        self.name = name
        self.detail = detail
