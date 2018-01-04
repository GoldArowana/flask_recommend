"""
@author:金龙
@school:hrbust
@depart:computer
@file: runserver.py
@time: 2017/12/26 18:44
@describe:
"""
from web import app
import logging
from logging.handlers import RotatingFileHandler


def set_logger():
    info_file_handler = RotatingFileHandler('D:\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('D:\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('D:\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == '__main__':
    set_logger()
    app.run(host='0.0.0.0', debug=True, port=80, threaded=True)
