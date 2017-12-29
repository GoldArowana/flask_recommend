"""
@author:金龙
@school:hrbust
@depart:computer
@file: topic_control.py
@time: 2017/12/29 11:24
@describe:
"""
from flask import render_template, jsonify, redirect, request
from flask_sqlalchemy import BaseQuery

from web import app, db
from python.model.Topic import Topic  # type:Topic
from sqlalchemy.sql import func


@app.route('/topic/<int:page>/', methods={'get', 'post'})
def topic(page):
    baseQuery = Topic.query.order_by(Topic.on_datetime.desc())  # type:BaseQuery
    paginate = baseQuery.paginate(page=page, per_page=4)
    topic_list = paginate.items
    ret_dic = {'topics': []}
    for item_topic in topic_list:  # type:Topic.Topic
        ret_dic['topics'].append(
            {'id': item_topic.id, 'title': item_topic.title, 'company': item_topic.company.name,
             'context': item_topic.context, 'tag': item_topic.tag,
             'time': item_topic.on_datetime, 'author': item_topic.user.username})
    ret_dic['cur_page'] = page
    ret_dic['has_prev'] = paginate.has_prev
    ret_dic['has_next'] = paginate.has_next
    return render_template('topic.html', ret_dic=ret_dic)


@app.route('/topic/publish/', methods={'get', 'post'})
def topic_publish():
    return render_template('publish.html', methods={'get', 'post'})


@app.route('/topic/detail/<int:topic_id>/', methods={'get', 'post'})
def detail(topic_id):
    topic = Topic.query.filter_by(id=topic_id).first()
    ret_dic = {'company': topic.company.name, 'author': topic.user.username, 'time': topic.on_datetime,
               'context': topic.context, 'title': topic.title, 'tag': topic.tag}
    print(ret_dic)
    return render_template('detail.html', ret_dic=ret_dic)


@app.route('/get_topic_count/', methods={'get', 'post'})
def get_topic_count():
    topic_count = db.session.query(func.count('*')).select_from(Topic).scalar()
    return jsonify(topic_count)


@app.route('/topic/new/', methods={'get', 'post'})
def topic_new():
    title = request.values.get('title')
    context = request.values.get('context')

    return redirect('/')
