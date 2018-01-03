"""
@author:金龙
@school:hrbust
@depart:computer
@file: email_control.py
@time: 2018/1/3 23:20
@describe:
"""
from web import app
from flask import jsonify, request
from random import randint
import smtplib
from email.mime.text import MIMEText

msg_from = '1015486437@qq.com'  # 发送方邮箱
password = 'tffavpchpuznbfed'  # 填入发送方邮箱的授权码

try:
    ss = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
    ss.login(msg_from, password)
except smtplib.SMTPException as e:
    print("登陆失败")


@app.route('/get_sign/', methods={'post'})
def get_sign():
    msg_to = request.values.get('email_address')  # 收件人邮箱
    print(msg_to)
    msg = MIMEText("这里是验证码" + str(randint(10000, 90000)))  # 正文
    msg['Subject'] = "金龙:欢迎来到理工内推系统"  # 主题
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        ss.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    return jsonify({'time': 120});
