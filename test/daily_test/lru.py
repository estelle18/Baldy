#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/20 9:57
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : lru.py
@Url     : https://leetcode.cn/problems/lru-cache/
@Software: PyCharm
"""


# 双链表插入删除设计
# 哨兵节点被用作伪头，伪尾结点始终存在
class ListNode(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.Lru = dict()

        # 使用伪头部和伪尾部节点
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key):
        if key not in self.Lru:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        cur_node: ListNode = self.Lru[key]
        self.move_to_head(cur_node)
        return cur_node.val

    def put(self, key, value):
        # 当key存在时，需要做与get方法种同样的操作, 并替换值
        if key in self.Lru:
            del_node: ListNode = self.Lru[key]
            del_node.val = value
            self.move_to_head(del_node)
        else:
            # 创建待插入结点
            cur_node: ListNode = ListNode(key, value)
            # 必须先插入链表以及hash表中，否则会出现none无法进行下去
            self.Lru[key] = cur_node
            self.insert_head(cur_node)
            self.size += 1
            # 查看缓存是否已满
            if self.capacity < self.size:
                # 删除尾结点以及hash表的key-value
                del_node = self.delete_tail()
                self.Lru.pop(del_node.key)
                self.size -= 1

    # 头插法，在双向链表头部插入结点：O（1）
    def insert_head(self, insert: ListNode):
        insert.prev = self.head
        insert.next = self.head.next
        # head的下一个结点的前驱是insert
        self.head.next.prev = insert
        self.head.next = insert

    # 删除给定结点
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 命中后，需要删除后再重新插入到头部
    def move_to_head(self, hit_node):
        self.remove_node(hit_node)
        self.insert_head(hit_node)

    # 尾删，容量满了之后，需要删除尾部结点再做头插
    def delete_tail(self):
        # 尾部结点是伪结点，其prev即为Lru的最后一个结点
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node

cache = LRU(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
