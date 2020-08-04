# -*- coding:utf-8 -*-

import uuid
import random
import time
from datetime import datetime


class QuickSqlBuilder(object):
    def __init__(self):
        super(QuickSqlBuilder, self).__init__()

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
        with open("./sql/insert_user_500w.sql", "w+") as f, open("./sql/insert_order_500w+.sql", "w+") as f1:
            for x in range(1000):
                insert_user_sql = "insert into `user` ( `id`,`user_name`,`age`, `phone`, `province`, `city`, `create_time`,`update_time` ) values "
                insert_order_sql = "insert into `order` ( `id`, `product_count`, `user_id`, `price`, `create_time`, `update_time`) values "
                user_values, order_values = [], []
                for i in range(5000):
                    timestamp = self.randomTimestamp()
                    time_local = time.localtime(timestamp)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                    user_id = str(uuid.uuid4())
                    user_values.append(
                        (user_id, "名字" + str(x) + str(i),
                         random.randint(1, 120), self.createPhone(),
                         str(random.randint(1, 26)),
                         str(random.randint(1, 1000)), create_time,
                         create_time))
                    random_order_count = random.randint(0, 3)
                    if random_order_count > 0:
                        for c in range(random_order_count):
                            timestamp = self.randomTimestamp()
                            time_local = time.localtime(timestamp)
                            order_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                            order_values.append((str(uuid.uuid4()), random.randint(1, 5), user_id,
                                                 random.randint(10, 2000), order_create_time, order_create_time))

                user_values_str = str(user_values).strip('[]')
                insert_user_sql += user_values_str
                f.write(insert_user_sql)
                f.write(";\n")

                order_values_str = str(order_values).strip('[]')
                insert_order_sql += order_values_str
                f1.write(insert_order_sql)
                f1.write(";\n")


if __name__ == "__main__":
    quickInsert = QuickSqlBuilder()
    startTime = datetime.now()
    print("开始时间", startTime)
    quickInsert.insert_data()
    endTime = datetime.now()
    print("结束时间", endTime, "共持续", (endTime - startTime).seconds, "秒")
