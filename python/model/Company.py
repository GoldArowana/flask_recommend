"""
@author:金龙
@school:hrbust
@depart:computer
@file: Company.py
@time: 2017/12/26 21:05
@describe:公司
"""

from web import db


class Company(db.Model):
    __tablename__ = 'company'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(50), nullable=False)
    alias = db.Column(db.VARCHAR(50), nullable=True)
    logo_image = db.Column(db.Integer, db.ForeignKey('image.id'))
    detail = db.Column(db.TEXT)

    topics = db.relationship("Topic", backref='company')

    def __init__(self, name, alias=''):
        self.name = name
        self.alias = alias
