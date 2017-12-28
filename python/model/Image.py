"""
@author:金龙
@school:hrbust
@depart:computer
@file: Picture.py
@time: 2017/12/26 21:07
@describe:图片
"""

from web import db


class Image(db.Model):
    __tablename__ = 'image'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.VARCHAR(255), unique=True,nullable=False)
    detail = db.Column(db.VARCHAR(255))
