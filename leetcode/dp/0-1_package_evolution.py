#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/10 23:42
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : 0-1_package_evolution.py
@Url     : https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tqId=21239&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
@Software: PyCharm
"""

'''
1. 0-1背包
'''
def paclage_0_1():
    # n为总钱数，即0-1背包的总重量，m为物品数
    n, m = map(int,input().split())
    primary, annex = {}, {}
    for i in range(1,m+1):
        x, y, z = map(int, input().split())
        if z==0:#主件
            primary[i] = [x, y]
        else:#附件
            if z in annex:#第二个附件
                annex[z].append([x, y])
            else:#第一个附件
                annex[z] = [[x,y]]
    m = len(primary)#主件个数转化为物品个数

    # 1.初始化状态数组
    # 定义为有m个物品n的容量时，背包价值最大的装法
    dp = [[0]*(n+1) for _ in range(m+1)]
    # 0-1背包的思路
    # for i in range(1,m+1):
    #     for j in range(1,n+1):
              # 背包容量j下，判断第i件物品的容量是否小于容量j
              # 如果小于，则装入，价值肯定变大，否则还是i-1件的价值
    #         if j-w[i]>=0:
    #             dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
    #         else:
    #             dp[i][j] = dp[i-1][j]

    w, v= [[]], [[]]
    for key in primary:
        w_temp, v_temp = [], []
        w_temp.append(primary[key][0])#1、主件
        v_temp.append(primary[key][0]*primary[key][1])
        if key in annex:#存在附件【3种情况】
            w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
            v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1])
            if len(annex[key])>1:#存在两附件
                w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
                v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
                w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#3、主件+附件1+附件2
                v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
        w.append(w_temp)
        v.append(v_temp)
    # m 为物品数
    for i in range(1,m+1):
        # j 当前钱数的情况下是否可买第 i 个主件
        for j in range(10,n+1,10): # 都是 10 元的整数倍
            max_i = dp[i-1][j]
            for k in range(len(w[i])): # 存在多个附件情况，判断应该是否应该放入对应的附件
                if j-w[i][k]>=0:
                    max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
            dp[i][j] = max_i
    print(dp[m][n])

'''
2. 最长回文子串
'''
def longSym():
    input_str = input()
    len_str = len(input_str)

    if len_str < 2: print(1)
    if len_str == 2 and input_str[0] == input_str[1]: print(2)
    # 1.遍历所有可能长度的子序列
    # 2.判断该序列是否为回文串
    #    长度为1：一定时回文串：true
    #    长度为2：左右相等：true，否则，false
    #    其他长度情况：p[i+1,j-1] && s[i]==s[j]:true
    # 3. 记下当前最大长度的值
    max_string_len = 0
    result_string = ""

    # 先初始化dp矩阵,dp[i,j]表示字符串s[i:j]是否为回文子串
    # 需要记下下标，进行对比
    dp = [[False] * len_str for _ in range(len_str)]
    for i in range(1, len_str + 1):
        for left in range(len_str):
            right = left + i - 1  # 查找字符串右下标
            if right >= len_str: break  # 一旦右下标大于等于字符串长度会产生越界跳出
            dp[left][right] = (i == 1) or ((i == 2) and (input_str[left] == input_str[right])) or (dp[left + 1][right - 1] and (input_str[left] == input_str[right]))
        if (dp[left][right] and i > max_string_len):
            max_string_len = i
            result_string = input_str[left:right + 1]
    print(len(result_string))

'''
3. 最小编辑距离
'''
import numpy as np
str1 = 'abcd'
str2 = 'abcde'

# 1. 定义转移状态矩阵 dp[i][j]:表示str1[:i]与str2[:j]的最小编辑距离
dp = [[x for x in range(len(str2))] for y in range(len(str1))]
# 2. 初始化 dp矩阵的值，第0行和第0列表示str[:i]与空字符串的编辑距离
for i in range(len(str1)):
    dp[i][0] = i
print(np.array(dp))

