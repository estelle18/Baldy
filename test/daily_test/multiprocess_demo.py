#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/13 20:31
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : multiprocess_demo.py
@Url     : 
@Software: PyCharm
"""
# import queue  不能进行多进程之间的数据传输
# from multiprocessing import Queue   借助Queue解决生产者消费者模型队列是安全的。自带锁

from multiprocessing import Queue, Process
from time import sleep

# q = Queue(3)  # num 队列的最大长度，为一个数字
# q.get()  # 阻塞等待获取数据，如果有数据直接获取，如果没有数据，阻塞等待
# q.put()  # 阻塞，如果可以直接往队列中放数据，就直接放，如果不能放，就阻塞等待
#
# q.get_nowait()  # 不阻塞，如果有数据直接获取，没有数据就报错
#
# q.put_nowait()  # 不阻塞，如果可以继续往队列中放数据，就直接放，不能放就报错

# q.put(123)
# q.put("abc")
# q.put([4, 5, 6])
# q.put_nowait(999)
# print(q.get())
# print(q.get())
# print(q.get())

def consumer(q, name):
    while 1:
        info = q.get()
        if info:
            print('%s 拿走了%s' % (name, info))
        else:  # 当消费者获得队列中数据时，如果获得的是None，就是获得到了生产者不再生产数据的标识
            break  # 此时消费者结束即可


def producer(q, product):
    for i in range(5):
        info = '生产了' + product + '版的娃娃%s号' % str(i)
        q.put(info)
        print(info)
    q.put(None)  # 让生产者生产完数据后，给消费者一个不再生产数据的标识


if __name__ == '__main__':
    q = Queue(5)
    pro = Process(target=producer, args=(q, '波多小姐'))
    con = Process(target=consumer, args=(q, '苍老师'))
    pro.start()
    con.start()