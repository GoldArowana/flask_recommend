"""
@author:金龙
@school:hrbust
@depart:computer
@file: Advertising.py
@time: 2017/12/26 21:06
@describe:广告
"""
from flask_sqlalchemy import SQLAlchemy

from web import db  # type: SQLAlchemy
from datetime import date


class Advertising(db.Model):
    __tablename__ = 'advertising'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    editor_id = db.Column(db.Integer, db.ForeignKey('manager.id'), nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)
    html = db.Column(db.TEXT)

    def __init__(self, company_id, editor_id, from_date=date.today(), to_date=date.today(), html=''):
        self.company_id = company_id
        self.editor_id = editor_id
        self.from_date = from_date
        self.to_date = to_date
        self.html = html

    def __repr__(self):
        return "<Advertising id:%d, company_id:%d, editor_id:%d>" % (self.id, self.company_id, self.editor_id)
