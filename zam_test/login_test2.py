"""
@author:金龙
@school:hrbust
@depart:computer
@file: login_test2.py
@time: 2018/1/4 18:37
@describe:
"""
import functools


def trace(func):
    @functools.wraps(func)
    def wrapper():
        func()

    return wrapper


@trace
def square():
    print('123')


square()
