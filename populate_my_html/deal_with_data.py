import mysql.connector,logging, copy, os



class DIR():
    def __init__(self, dir_name):
        self.name = dir_name
        self.file_quantity = 0
        self.files= []
    def getFileName(self):
        dirs = os.listdir(self.name)
        for f in dirs:
            self.files.append(f)
            self.file_quantity += 1
    def __str__(self):
        return 'dir:%s\tquantity of files:%s' %(self.name, self.file_quantity)

class File():
    def __init__(self, dirname,filename):
        self.name = filename
        self.path = dirname+filename
        self.size = 0
    def getContent(self):
        with open(self.path) as file:
            try:
                self.content = file.read()
                self.size = os.path.getsize(self.path)
            except Exception as e:
                logging.error(e)
                self.content = ''


def getFileset(total_files, exit_files): #exit_files 为列表，元素为元组
    exit_files = set(exit_files)
    total_files = set(total_files)
    total_files_cp = copy.deepcopy(total_files)
    for file in exit_files:
        if file[0] in total_files:
            total_files_cp.remove(file[0])
    return (total_files_cp)

# def getValues(total_files):
#     global values
#     for file in total_files:
#         my_file = File(dirs.name, file)
#         my_file.getContent()
#         value = ( my_file.name, my_file.size, my_file.content)
#         values.append(value)
#         # print('in getValues,values: %s' % values)

def Insert(total_files):
    global count
    values = []
    sql = "insert into html( file_name,size, content)  \
                                        value( %s, %s, %s);"
    loop = len(total_files)/1000
    circu = 1
    for file in total_files:
        my_file = File(dirs.name, file)
        my_file.getContent()
        value = (my_file.name, my_file.size, my_file.content)
        values.append(value)
        if  circu <= loop and len(values) == 1000:  #每次插入一千条
            try:
                cur.executemany(sql,values)
                db.commit()
                circu += 1
                count += 1000
                logging.info('Process[%s] insert files:%s' %(sys.argv[1], count))
            except Exception as e:  #批量插入失败，改为每次插入一条
                logging.error(e)
                once_insert_one(values)
                circu += 1
            values = []
            if count % 1000 == 0:
                logging.info('Process[%s] insert files:%s' %(sys.argv[1], count))

        if circu > loop and len(values) == (len(total_files) % 1000):   #不足1000个
            try:
                cur.executemany(sql,values)
                db.commit()
                circu += 1
                count += len(values)
            except Exception as e:  #批量插入失败，改为每次插入一条
                logging.error(e)
                once_insert_one(values)
            values = []



def once_insert_one(values):
    # global count,failed_insert_files,values
    # print('\tmyInsert,values:', values)
    sql_insert_one = "insert into html( file_name,size, content)  \
                                    value( '%s', '%s', '%s');"
    global failed_insert_files, count
    for value in values:
        try:
            # print(sql_insert_one %(value))
            cur.execute(sql_insert_one %(value))
            count = count + 1
        except Exception as e:
            logging.error('Process[%s] %s\tfailed insert %s' %(sys.argv[1],e, value[0]))
            failed_insert_files += ('%s in %s\n' %(e, value[0]))
            continue
        # if count % 1000 == 0:
        #     db.commit()
            # logging.info('Process[%s] insert files: %s' % (sys.argv[1],count))

    # print('\tmyInsert, count: %s' % count)




def transaction_insert(total_files):
    # getValues(total_files)
    # myInsert()
    # print('in transaction_insert,count: %s' % count)
    Insert(total_files)
    return count


if __name__ == '__main__':
    import logging.config, os, sys, json
    from send_mail import mail
    from config import Args
    args = Args()

    worker_id = int(sys.argv[1])

    logging.basicConfig(
        filename='mylog.log',
        level=logging.INFO,
        format='%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s] %(filename)s[line:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    try:
        db = mysql.connector.connect(host=args.host, user=args.username, password=args.password,charset='utf8')
        # db = mysql.connector.connect(user='root', password='hua1995225', charset='utf8')
        logging.info('Process[%s] 成功连接数据库' %sys.argv[1])
    except Exception as e:
        logging.error('%s' % e)
        mail(msg_text=('Process[%s]\t%s' %(sys.argv[1], e)), msg_from='deal_with_data.py')

    cur = db.cursor()

    try:
        cur.execute('use html_db')
        # logging.info('Process[%s] create database html_db successed ;' %sys.argv[1])
    except Exception as e:
        logging.error('Process[%s] create database failed:%s' % (sys.argv[1],e))
        mail(msg_text=('Process[%s]\t%s' %(sys.argv[1], e)), msg_from='deal_with_data.py')


    # try:
    #     cur.execute('use html_db;')
    #     cur.execute('set autocommit=0;')
    #     # cur.execute("drop table if exists html;")
    #     cur.execute("create table html( file_name   varchar(64)    NOT NULL,\
    #                                     size        varchar(8)     NOT NULL,\
    #                                     content     text(204800)   NOT NULL)\
    #                                     ENGINE = InnoDB DEFAULT CHARSET=UTF8;")
    #     cur.execute('ALTER TABLE html ADD PRIMARY KEY (file_name);')
    #     logging.info('Process[%s] create table successed' % sys.argv[1])
    # except Exception as e:
    #     logging.error('Process[%s] %s'%(sys.argv[1],e))

    dirs = DIR(args.dirs)
    # dirs.getFileName()             #获取目录中所有文件名
    # print(dirs)
    # logging.info('%s files in %s\tbegin to insert' %(dirs.file_quantity, dirs.name))
    # cur.execute("select file_name from html;")
    # db_files = cur.fetchall()  # 获取已插入到数据库中的文件名
    # print(db_files)
    with open('waiting_insert_files.txt','r', encoding='utf8') as file:
        total_waiting_insert_files = json.load(file)

    waiting_insert_files = [item for item in total_waiting_insert_files if (ord(item[7]))%10 == worker_id]
    logging.info('Process[%s] waiting_insert_files: %s' % (sys.argv[1], len(waiting_insert_files)))
    # print(len(waiting_insert_files))

    failed_insert_files = ''
    # print('waiting_insert_files: %s' % waiting_insert_files)

    sql = "insert into html(file_name,size, content)  \
                                    value( '%s', '%s', '%s');"
    values = []
    count = 0
    try:
        count = transaction_insert(waiting_insert_files)
        db.commit()
    except Exception as e:
        logging.error('Process[%s] %s' %(sys.argv[1],e))
        mail(msg_text=('Process[%s]\t%s' %(sys.argv[1], e)), msg_from='deal_with_data.py')

    if failed_insert_files != '':  #有插入失败的文件
        with open('failed_insert_files.txt','a', encoding='utf8') as file:
            file.write(failed_insert_files)
    # cur.execute("select count(file_name) from html;")
    # db_files = cur.fetchall()[0][0]  # 获取已插入到数据库中的文件数
    logging.info('Process[%s] Finished\t waiting_insert_files: %s\tinsert %s files successed' % (sys.argv[1],len(waiting_insert_files),count))
    msg = 'Process[%s] Finished\t waiting_insert_files: %s\ninsert %s files successed' % (sys.argv[1],len(waiting_insert_files),count)
    mail(msg_subject='运行结束',msg_text=msg)
    db.close()





