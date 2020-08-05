# -*- coding:utf-8 -*-

import uuid
import random
import time
from datetime import datetime
import pymysql as mysql
import threading

host = "127.0.0.1"
port = 3306
username = "root"
password = "P@ssw0rd"
charset = "utf-8"
db = "mast_slave"


class QuickThreadsInsert(object):
    def __init__(self):
        super(QuickThreadsInsert, self).__init__()

    @staticmethod
    def connect():
        return mysql.connect(host=host, port=port, user=username, passwd=password, db=db)

    def strTimeProp(self, start, end, prop, frmt):
        stime = time.mktime(time.strptime(start, frmt))
        etime = time.mktime(time.strptime(end, frmt))
        ptime = stime + prop * (etime - stime)
        return int(ptime)

    def randomTimestamp(self, frmt='%Y-%m-%d %H:%M:%S'):
        start = '2016-06-02 12:12:12'
        end = '2020-07-27 00:00:00'
        return self.strTimeProp(start, end, random.random(), frmt)

    def createPhone(self):
        for k in range(10):
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                       "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                       "186", "187", "188", "189"]
            return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    def insert_data(self):
        cursor = self.conn.cursor()
        for x in range(1000):
            insert_user_sql = """
            insert into `user` ( `id`,`user_name`,`phone`,`age`, `province`, `city`, `create_time`,`update_time` )
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                """
            insert_order_sql = """ insert into `order` ( `id`, `product_count`, `user_id`, `price`, `create_time`, `update_time`) 
                               values(%s,%s,%s,%s,%s,%s)
                               """
            user_values, order_values = [], []
            for i in range(1000):
                timestamp = self.randomTimestamp()
                time_local = time.localtime(timestamp)
                createTime = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                user_id = str(uuid.uuid4())
                user_values.append(
                    (user_id, "名字" + str(x) + str(i), self.createPhone(), random.randint(1, 120),
                     str(random.randint(1, 26)),
                     str(random.randint(1, 1000)), createTime, createTime))

                random_order_count = random.randint(0, 3)
                if random_order_count > 0:
                    for c in range(random_order_count):
                        timestamp = self.randomTimestamp()
                        time_local = time.localtime(timestamp)
                        order_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                        order_values.append((str(uuid.uuid4()), random.randint(1, 5), user_id,
                                             random.randint(10, 2000), order_create_time, order_create_time))
            cursor.executemany(insert_user_sql, user_values)
            cursor.executemany(insert_order_sql, order_values)
            self.conn.commit()

        cursor.close()


class InsertThread(threading.Thread):

    def __init__(self, name=None):
        threading.Thread.__init__(self, name=name)

    def run(self):
        startTime = datetime.now()
        print(threading.current_thread().name + "开始时间" + str(startTime))
        quickInsert = QuickThreadsInsert()
        quickInsert.conn = QuickThreadsInsert.connect()
        quickInsert.insert_data()
        endTime = datetime.now()
        print(threading.current_thread().name + "结束时间" + str(endTime) + "," + "共持续" + str(
            (endTime - startTime).seconds) + "秒")


if __name__ == "__main__":
    for i in range(5):
        t = InsertThread(name="线程" + str(i))
        t.start()
