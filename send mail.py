# -*- coding: utf-8 -*- 
# @Time : 2020/2/4 下午6:39 
# @Author : lily
# @File : send mail.py

import smtplib

from email.mime.text import MIMEText

# ------1.跟发件相关的参数-----
smtpserver = "smtp.qq.com"
port = 465
sender = "554784810@qq.com"
psw = "yopakcxakkndbbgf"
receiver = "554784810@qq.com"

# -----2.编辑邮件内容----
subject = "这个是QQ主题"
body = '<p>这个是发送的QQ邮件</p>'
msg = MIMEText(body,"html","utf-8")
msg['from']=sender
msg['to']= "554784810@qq.com"
msg['subject']=subject

# --------3.qq邮箱发送邮件------
smtp = smtplib.SMTP_SSL(smtpserver,port)
smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

# ---兼容两种方式发送邮件----
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

