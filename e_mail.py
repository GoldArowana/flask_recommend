"""
@author:金龙
@school:hrbust
@depart:computer
@file: email.py
@time: 2017/12/29 17:28
@describe:
"""

# -*-coding:utf-8-*-
# ==========================================
# 导入smtplib和MIMEText
# ==========================================
from random import randint
import smtplib
from email.mime.text import MIMEText

msg_from = '1015486437@qq.com'  # 发送方邮箱
password = 'tffavpchpuznbfed'  # 填入发送方邮箱的授权码
msg_tos = ['504471340@qq.com', '609429765@qq.com', '1015486437@qq.com']  # 收件人邮箱
for i in range(len(msg_tos)):
    msg_to = msg_tos[i]
    subject = "金龙:欢迎来到理工内推系统"  # 主题
    content = "这里是验证码" + str(randint(10000, 90000))  # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        ss = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
        ss.login(msg_from, password)
        for i in range(1, 10):
            ss.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        ss.quit()
