"""
@author:金龙
@school:hrbust
@depart:computer
@file: manage.py
@time: 2017/12/26 18:44
@describe:
"""

from web import db, app
from python.model import *
from python.model import Manager as Man  # 因为这里的Manager和flask_script里的Manager重名了，所以起一个别名
from flask_script import Manager
from datetime import datetime
from random import randint

manager = Manager(app)


@manager.command
def run_test():
    # init_database()
    print('run test.....')
    db.drop_all()
    db.create_all()

    # 插入管理员Manager
    db.session.add(Man.Manager('wei', '123'))
    db.session.add(Man.Manager('song', '123'))
    # 插入用户User
    db.session.add(User.User('king', '123'))
    db.session.add(User.User('hang', '123'))
    db.session.add(User.User('chen', '123'))
    db.session.add(User.User('sun', '123'))
    db.session.add(User.User('liu', '123'))
    db.session.add(User.User('zhu', '123'))
    # 插入公司Company
    db.session.add(Company.Company('百度', '熊场'))
    db.session.add(Company.Company('腾讯', '鹅场'))
    db.session.add(Company.Company('网易', '猪场'))
    db.session.add(Company.Company('京东', '狗场'))
    db.session.add(Company.Company('去哪儿网', '驼场'))
    # 插入个人简历
    user_list = User.User.query.all()
    for i in user_list:  # type:User.User
        db.session.add(Resume.Resume(i.id, detail=i.username + '的简历'))
    # 插入广告和主题
    man = Man.Manager.query.get(1)  # type:Man.Manager
    user = User.User.query.get(1)
    company_list = Company.Company.query.all()
    for i in company_list:  # type:Company.Company
        # 插入广告
        db.session.add(
            Advertising.Advertising(i.id, man.id, from_date=datetime(2017, 12, 30), to_date=datetime(2018, 10, 1),
                                    html='<h1>你好' + i.name + '的广告</h1>----' + man.username + "编辑"))
        # 插入主题Topic
        for j in range(0, 4):
            db.session.add(Topic.Topic(i.id, user.id, on_datetime=datetime(2017, randint(1, 12), randint(1, 25)),
                                       context=user.username + "发起：" + i.name + '公司开始' + str(j) + '次招聘招聘啦',
                                       title=i.name + '公司的xxx职位', tag='18届,19届,寒假实习'))
    # 插入评论
    topic_list = Topic.Topic.query.all()
    for i in topic_list:  # type:Topic.Topic
        for j in user_list:  # type: User.User
            db.session.add(Comment.Comment(i.id, j.id, context='我是' + j.username + ',我想投简历'))

    db.session.commit()


if __name__ == '__main__':
    manager.run()
