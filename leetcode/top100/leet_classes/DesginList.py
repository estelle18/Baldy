#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/19 16:08
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : DesginList.py
@Url     : 
@Software: PyCharm
"""
# Definition for singly-linked list.
# 哨兵节点被用作伪头始终存在
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 单链表：最简单的链表
class MyLinkedList():
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
