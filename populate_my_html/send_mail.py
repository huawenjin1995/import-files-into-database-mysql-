import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def mail(sender='1163824714@qq.com', password='neaxeqmduktrhcdj', receiver='1163824714@qq.com', msg_text='运行失败', \
         msg_from='huawenjin', msg_to = 'huawenjin', msg_subject='警报', server_smtp='smtp.qq.com', server_port=465):
    '''
    :param sender: 发件人邮箱地址
    :param password: 发件人邮箱密码
    :param receiver: 收件人邮箱（可以发送给自己)
    :param msg_text: 邮件文本内容（字符串）
    :param msg_from: 发件人邮箱昵称（字符串）
    :param msg_to: 收件人邮箱昵称(字符串）
    :param msg_subject: 邮件的主题，也可以说是标题
    :param server_smtp: 发件人邮箱中的SMTP服务器
    :param server_port: 发件人邮箱中的SMTP服务器端口
    :return:
    '''
    ret = True
    try:
        msg = MIMEText(msg_text, 'plain', 'utf-8')
        msg['From'] = formataddr([msg_from, sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([msg_to, receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = msg_subject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(server_smtp, server_port)  # 发件人邮箱中的SMTP服务器，端口
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret



if __name__ == '__main__':
    sender = '1163824714@qq.com'
    password = 'neaxeqmduktrhcdj'
    receiver = '277143607@qq.com'
    msg_text = open('../advanced_topics_of_mod/my_file.py').read()
    msg_from = 'deal_with_data.py'
    msg_to = 'huawenjin'
    msg_subject = '警报:deal_with_data.py运行失败'
    server_smtp = "smtp.qq.com"
    server_port = 465

    ret = mail(sender= sender, password= password, receiver= receiver, msg_text= msg_text, msg_from= msg_from, msg_to= msg_to,\
               msg_subject= msg_subject, server_smtp= server_smtp, server_port= server_port)
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")