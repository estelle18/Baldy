#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/7 16:09
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : ListNode.py
@Url     : 
@Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        # 先初始化一个头节点，为None
        self.head = None

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头结点
        # 这个节点创建完，包含两部分：是个既包含节点值，也包含节点所链接的下一个节点
        self.head = ListNode(data[0])

        # 初始化p指向头节点
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            # 构建完一个节点，移动到构建完的节点上，继续向后构建节点
            p = p.next
        return self.head

    # 遍历链表
    def traveList(self):
        # if self.isEmpty():
        #     exit(0)
        print("link list traveling result:")
        p = self.head
        while p:
            print(p.val)
            p = p.next
