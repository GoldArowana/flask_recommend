"""
@author:金龙
@school:hrbust
@depart:computer
@file: usertest.py
@time: 2017/12/27 15:10
@describe:
"""
from datetime import date


class UserTest(object):
    id: int
    age: int
    old = 1

    def __init__(self, id, age, old):
        self.id = id
        self.age = age
        self.old = old

    def print(self):
        print(self.id)
        print(self.age)
        print(self.old)

        print(UserTest.old)


u = UserTest(3, 5, 7)
u.print()
UserTest.old = 111
t = UserTest(4, 8, 9)
t.print()
if __name__ == '__main__':
    print(date.today())
