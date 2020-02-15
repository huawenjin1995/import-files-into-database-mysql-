

if __name__ == '__main__':
    import mysql.connector, logging
    from deal_with_data import DIR
    from send_mail import mail
    from config import Args
    dir = DIR('/home/huawenjin/learning_materials/python学习资料/html/')

    args = Args()
    try:
        db = mysql.connector.connect(host=args.host, user=args.username, password=args.password,charset='utf8')
        logging.info('成功连接数据库')
    except Exception as e:
        logging.error('%s' % e)
        mail(msg_text=e, msg_from='inquire_html_db.py')

    cur = db.cursor()

    try:
        cur.execute('use html_db;')
        cur.execute('select count(*) from html;')
        result = cur.fetchall()
        logging.info('dirs file: %s\ninsert file: %s' %(dir.file_quantity,result))
    except Exception as e:
        logging.error(e)

    msg = 'dirs file: %s\ninsert file: %s' %(dir.file_quantity,result)
    mail(msg_text=msg, msg_from='inquire_html_db.py')