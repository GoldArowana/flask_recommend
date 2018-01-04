"""
@author:金龙
@school:hrbust
@depart:computer
@file: vip.py
@time: 2018/1/4 14:28
@describe:
"""

from web import db


class Vip(db.Model):
    __tablename__ = 'vip'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vip_level = db.Column(db.Integer, server_default='0')
    remain_coin = db.Column(db.Integer, server_default='0')
    spent_coin = db.Column(db.Integer, server_default='0')

    def __init__(self, user_id, vip_level=0, remain_coin=0, spent_coin=0):
        self.user_id = user_id
        self.vip_level = vip_level
        self.remain_coin = remain_coin
        self.spent_coin = spent_coin

    def __repr__(self):
        return "<Vip id:%d, vip_level:%d, remain_coin:%d, spent_coin:%d>" % (
            self.id, self.vip_level, self.remain_coin, self.spent_coin)
