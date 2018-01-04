"""
@author:金龙
@school:hrbust
@depart:computer
@file: company_control.py
@time: 2018/1/4 15:36
@describe:
"""
from flask import render_template, jsonify, redirect, request, session
from flask_sqlalchemy import BaseQuery

from web import app, db
from python.model.Company import Company  # type:Company


@app.route('/get_company_inf/', methods={'get', 'post'})
def get_company_inf():
    company_list = Company.query.all()
    ret = []
    for i in company_list:  # type:Company
        ret.append({'id': i.id, 'name': i.name})
    return jsonify(ret)
