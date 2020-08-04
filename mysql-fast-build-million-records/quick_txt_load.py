# -*- coding:utf-8 -*-

import uuid
import random
import time
from datetime import datetime


class QuickTxtBuilder(object):
    def __init__(self):
        super(QuickTxtBuilder, self).__init__()

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
        with open("./sql/load_user_txt_500w.txt", "w+") as f, open("./sql/load_order_txt_500w+.txt", "w+") as f1:
            for x in range(1000):
                user_row_str, order_row_str = '', ''
                for i in range(5000):
                    timestamp = self.randomTimestamp()
                    time_local = time.localtime(timestamp)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                    user_id = str(uuid.uuid4())
                    user_row = "{0},{1},{2},{3},{4},{5},{6},{7}".format(user_id, "名字" + str(x) + str(i),
                                                                   random.randint(1, 120), self.createPhone(),
                                                                   str(random.randint(1, 26)),
                                                                   str(random.randint(1, 1000)), create_time,
                                                                   create_time)

                    random_order_count = random.randint(0, 3)
                    if random_order_count > 0:
                        for c in range(random_order_count):
                            timestamp = self.randomTimestamp()
                            time_local = time.localtime(timestamp)
                            order_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                            order_row = "{0},{1},{2},{3},{4},{5}".format(str(uuid.uuid4()), user_id, random.randint(1, 5),
                                                 random.randint(10, 2000), order_create_time, order_create_time)
                            order_row_str += str(order_row) + "\n"

                    user_row_str += str(user_row) + "\n"

                f.write(user_row_str)
                f1.write(order_row_str)


if __name__ == "__main__":
    quickInsert = QuickTxtBuilder()
    startTime = datetime.now()
    print("开始时间", startTime)
    quickInsert.insert_data()
    endTime = datetime.now()
    print("结束时间", endTime, "共持续", (endTime - startTime).seconds, "秒")
