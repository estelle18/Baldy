#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/7 18:07
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_12_generateParenthesis.py
@Url     : https://leetcode-cn.com/problems/generate-parentheses/
@Software: PyCharm
"""


def generateParenthesis( n):
    res = []
    cur = ''

    # 借助系统栈,做加法,左括号使用数量一定要大于等于右括号的使用数量才可以
    def dfs(cur, left, right):
        if left == n and right == n:
            res.append(cur)
            return
        if left < right: return
        if left < n:
            dfs(cur + '(', left + 1, right)
        if right < n:
            dfs(cur + ')', left, right + 1)

    dfs(cur, 0, 0)
    return res


def generateParenthesis3(n):
    res = []
    cur = ''
    if n==0: return ''
    # 广度优先遍历，需自己创建队列进行辅助操作

    queue= [['',0,0]]
    while len(queue)>0:
        tmp = queue.pop()
        cur = tmp[0]
        left = tmp[1]
        right = tmp[2]
        if left == n and right == n:
            res.append(tmp[0])
            continue
        # 使用的右括号数大于左括号数,是违法的
        if left < right: continue
        if left < n:
            queue.append([cur+'(',left+1,right])
        if right <n:
            queue.append([cur+')',left,right+1])
    return res

print(generateParenthesis3(3))