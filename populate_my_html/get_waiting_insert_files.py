




if __name__ == '__main__':
    import mysql.connector, logging, json
    from send_mail import mail
    from deal_with_data import DIR, getFileset
    from config import Args

    logging.basicConfig(
        filename='mylog.log',
        level=logging.INFO,
        format='%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    args = Args()

    dirs = DIR(args.dirs)
    dirs.getFileName()             #获取目录中所有文件名

    try:
        db = mysql.connector.connect(host=args.host, user=args.username, password=args.password,charset='utf8')
        # db = mysql.connector.connect( user='root', password='hua1995225',charset='utf8')
        logging.info('成功连接数据库')
    except Exception as e:
        logging.error('%s' % e)
        msg = open('mylog.log').read()
        mail(msg_text=msg, msg_from='deal_with_data.py')

    cur = db.cursor()
    # try:
    #     cur.execute("create database html_db character set utf8mb4;")
    #     logging.info('create database html_db successed ;' )
    # except Exception as e:
    #     logging.error('create database failed:%s' % e)

    try:
        cur.execute('use html_db;')
        cur.execute('set autocommit=0;')
        cur.execute("drop table if exists html;")
        cur.execute("create table html( file_name   varchar(64)    NOT NULL,\
                                        size        varchar(8)     NOT NULL,\
                                        content     text(204800)   NOT NULL)\
                                        ENGINE = InnoDB DEFAULT CHARSET=UTF8;")
        cur.execute('ALTER TABLE html ADD PRIMARY KEY (file_name);')
        cur.execute('create index idx_filename on html(filename);')
        logging.info('create table successed')
    except Exception as e:
        logging.error(e)

    try:
        cur.execute("select file_name from html;")
        db_files = cur.fetchall()  # 获取已插入到数据库中的文件名
    except Exception as e:
        logging.info(e, 'can not get exists files in database')


    waiting_insert_files = getFileset(dirs.files, db_files)
    waiting_insert_files = list(waiting_insert_files)
    with open('waiting_insert_files.txt','w', encoding='utf8') as file:
        json.dump(waiting_insert_files, file)

    logging.info('total waiting insert files: %s' % len(waiting_insert_files))
