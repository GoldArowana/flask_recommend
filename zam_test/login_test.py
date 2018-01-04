"""
@author:金龙
@school:hrbust
@depart:computer
@file: login_test.py
@time: 2018/1/4 18:00
@describe:
"""


def login_require():
    def inner(func):
        def wrapper():
            print('before')
            func()
            print('after')

        return wrapper

    return inner


@login_require()
def hello():
    print('hello')


if __name__ == '__main__':
    hello()
