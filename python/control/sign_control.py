"""
@author:金龙
@school:hrbust
@depart:computer
@file: email_control.py
@time: 2018/1/3 23:20
@describe:
"""
from web import app, log
from flask import jsonify, request
from random import randint
import smtplib
from email.mime.text import MIMEText

import threading
import time


class SignHolder(threading.Thread):
    sign_list = [100] * 60

    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            SignHolder.sign_list.append(randint(100, 200 - 1))
            del SignHolder.sign_list[0]
            time.sleep(self.interval)

    def stop(self):
        self.thread_stop = True

    @staticmethod
    def sign(user_input):
        real_sign_num = int(user_input[0:4]) / int(user_input[4:])
        if real_sign_num in SignHolder.sign_list:
            return True
        return False


sign_holder = SignHolder(2)
sign_holder.setDaemon(True)
sign_holder.start()

msg_from = '1015486437@qq.com'  # 发送方邮箱
password = 'tffavpchpuznbfed'  # 填入发送方邮箱的授权码

try:
    ss = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
    ss.login(msg_from, password)
except smtplib.SMTPException as e:
    log("error", "email SMTP login failed")


@app.route('/get_sign/', methods={'post'})
def get_sign():
    msg_to = request.values.get('email_address')  # 收件人邮箱
    log("info", "start send email **********************************************************************")
    log("info", "send to:" + msg_to)
    ce = randint(1, 50)
    log("info", "ce:" + str(ce).zfill(2))
    base_sign_num = SignHolder.sign_list[59]
    try:
        msg = MIMEText("这里是验证码:" + str(SignHolder.sign_list[59] * ce).zfill(4) + str(ce).zfill(2))  # 正文
        log("info", "base_sign_num:" + str(base_sign_num))
        log("info", "这里是验证码:" + str(base_sign_num * ce).zfill(4) + str(ce).zfill(2))
        msg['Subject'] = "金龙:欢迎来到理工内推系统"  # 主题
        msg['From'] = msg_from
        msg['To'] = msg_to
        ss.sendmail(msg_from, msg_to, msg.as_string())
        log("info", "send success!**********************************************************************")
    except smtplib.SMTPException as e:
        log("error", "send failed!**********************************************************************")
    return jsonify({'time': 120})
