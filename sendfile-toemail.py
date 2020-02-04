# -*- coding: utf-8 -*- 
# @Time : 2020/2/4 下午7:13 
# @Author : lily
# @File : sendfile-toemail.py

import  smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMENonMultipart
from email.mime.text import MIMEText
# ------1.跟发件相关的参数-----
smtpserver = "smtp.qq.com"
port = 465
sender = "554784810@qq.com"
psw = "yopakcxakkndbbgf"
# receiver = "554784810@qq.com" #发送一个邮箱
receiver = ["554784810@qq.com","811677334@qq.com"] # 多个收件人使用list传值

# -----2.编辑邮件内容----
# 读文件
file_path = "ExampleReport.html"
with open(file_path, "rb") as fp:
    mail_body = fp.read()



# 邮件对象
msg = MIMEMultipart()
msg["from"] = sender  # 发件人
# msg["to"]=receiver  #一个收件人
msg["to"]= ";".join(receiver)  # 多个收件人list转str
msg["subject"]="测试发送附件"
msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")

# 邮件正文是MIMEText
body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="ExampleReport.html"'
msg.attach(att)
msg.attach(att)

#---兼容两种方式发送邮件----
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()



"""六：邮件收不到的几种原因：
1.Subject和正文内容不要用hello、hehe、test等单词
2.from(发件人)和to(收件人)不要为空，
  （要不然会被认为是垃圾邮件）
3.找不到的话，先看下垃圾信箱，是不是跑到垃圾箱了
4.如果前几次可以收到，后来收不到了，需改下subject内容
  （因为每次都是一个subject，系统也会拒收的，把subject内容设置为动态的是最好的）
5.部分邮箱是ssl加密了的，所以无法发送，如:qq邮箱
（用授权码去登录）
6.要是按照上面的步骤来报错了，说明代码抄错了，多检查几次。"""