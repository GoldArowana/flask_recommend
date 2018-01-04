"""
@author:金龙
@school:hrbust
@depart:computer
@file: vip_control.py
@time: 2018/1/4 15:55
@describe:
"""

from flask import render_template, jsonify, redirect, request, session
from flask_sqlalchemy import BaseQuery

from web import app, db
from python.model.Vip import Vip  # type:Vip
