"""
@author:金龙
@school:hrbust
@depart:computer
@file: runserver.py
@time: 2017/12/26 18:44
@describe:
"""
from web import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
