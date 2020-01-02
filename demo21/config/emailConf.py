import socket

import TickerConfig
from email.header import Header
from email.mime.text import MIMEText
import smtplib


def sendEmail(msg):
    """
    邮件通知
    :param str: email content
    :return:
    """
    # ret = True
    try:
        if TickerConfig.EMAIL_CONF["IS_MAIL"]:
            sender = TickerConfig.EMAIL_CONF["email"]
            receiver = TickerConfig.EMAIL_CONF["notice_email_list"]
            subject = '火车票查询'
            username = TickerConfig.EMAIL_CONF["username"]
            password = TickerConfig.EMAIL_CONF["password"]
            host = TickerConfig.EMAIL_CONF["host"]
            # s = "{0}".format(msg)
            # 对邮箱的配置进行整理：对于html和字符串，需要判断文本是否包含html标签
            import  re
            pattern = re.compile('.*?(<.*?>)')
            if pattern.search(msg):
                msg = MIMEText(str(msg), 'html', 'utf-8')  # 中文需参数‘utf-8’，发送html文档
            else:
                msg = MIMEText(str(msg), 'plain', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
            msg['Subject'] = Header(subject, 'utf-8')
            msg['From'] = sender
            msg['To'] = receiver
            # 创建smtp对象
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver.split(","), msg.as_string())
            # SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
            smtp.quit()
            print(u"邮件已通知, 请查收")
    except smtplib.SMTPException:
        # ret = False
        print ("Error: 无法发送邮件")
    # return ret

if __name__ == '__main__':

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">这是一个链接</a></p>
    """
    msg1 = 'code:D3112,tickent_num:11：start：shenzhen，end：hgh：time：xxx'
    sendEmail(msg1)
