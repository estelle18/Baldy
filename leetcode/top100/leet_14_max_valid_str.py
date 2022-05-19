#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/9 20:22
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_14_max_valid_str.py
@Url     : https://leetcode-cn.com/problems/longest-valid-parentheses/
@Software: PyCharm
"""

# 判断字符串括号是否有效
def is_valid_str(s_n):
    if s_n[-1] == '(' or s_n[0] == ')': return False

    stack = []
    for i in s_n:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True if len(stack) == 0 else False

print(is_valid_str(("(()))())(")))

# 1.暴力求解
def longestValidParentheses1(s):
    # 暴力求解【滑动窗口法】
    n = len(s) if len(s) % 2 == 0 else len(s) - 1

    # 判断当前字符串是否有效括号串
    def is_valid_str(s_n):
        if s_n[-1] == '(' or s_n[0] == ')': return False

        stack = []
        for i in s_n:
            if i == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False

    for i in range(n, 0, -2):
        for j in range(len(s)):
            if j + i <= len(s) and is_valid_str(s[j:j + i]):
                return i
    return 0

# 2. 动态规划
def longestValidParentheses2(s):
    if len(s)==0 : return 0
    max_len = 0
    dp = [0]*len(s)
    for i in range(1,len(s)):
        # if s[i] == ')' and i-dp[i-1]-1>0 and s[i-dp[i-1]-1] == '(':
        #     dp[i] = 2+dp[i-1]+dp[i-dp[i-1]-2]
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = dp[i-2]+2 if i>=2 else 2
            elif i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]
        max_len = max(max_len,dp[i])
    return max_len

# 3. 栈
def longestValidParentheses3(s):
    if len(s)==0 : return 0
    max_len = 0
    cur_len = 0
    # 初始化时匹配的长度一定小于0
    stack = [-1]
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                cur_len = i - stack[-1]
                max_len = max(max_len, cur_len)

    return max_len


print(longestValidParentheses3(")()())"))

print(4//2)