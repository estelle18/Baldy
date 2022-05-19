#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/7 16:10
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_11_mergeTwoLists.py
@Url     : https://leetcode-cn.com/problems/merge-two-sorted-lists/
@Software: PyCharm
"""

from leetcode.top100.leet_classes.ListNode import *
# 创建对象
d1 = [1,2,4]
d2 = [1,3,4]

list1=LinkList().initList(d1)
list2=LinkList().initList(d2)

#  递归方法
def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

print(mergeTwoLists(list1,list2))

#  迭代方法
# 设置哑结点以及移动指针
def mergeTwoLists2(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    dummy = prev = ListNode(-101)
    while list1 and list2:
        if list1.val > list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    prev.next = list1 if list1 is not None else list2
    return dummy.next



print(mergeTwoLists2(list1,list2))

print(55>>1)