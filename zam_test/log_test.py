"""
@author:金龙
@school:hrbust
@depart:computer
@file: log.py
@time: 2018/1/4 17:01
@describe:
"""


def login_require(level, *args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            print(level, 'before calling ', func.__name__)
            print(level, 'args', args, 'kvargs', kvargs)
            func(*args, **kvargs)
            print(level, 'end calling ', func.__name__)

        return wrapper

    return inner


@login_require(level='INFO')
def hello(name, age):
    print('hello', name, age)


if __name__ == '__main__':
    hello(name='nowcoder', age=2)  # = log(hello())
    print('*****************')
    hello('k', 23)
