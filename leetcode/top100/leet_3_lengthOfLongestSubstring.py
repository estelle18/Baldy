#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 16:24
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_3_lengthOfLongestSubstring.py
@url     : https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
@Software: PyCharm
"""
s = "abcabcbb"
# 滑动窗口
# tmp = []
max_substring_len = 0
# test_index = 0
# i = 0
# while i < len(s):
#     if s[i] not in tmp:
#         tmp.append(s[i])
#         max_substring_len = max(len(tmp), max_substring_len)
#         i += 1
#     else:
#         test_index += 1
#         i = test_index
#         tmp = []
#
# print(max_substring_len)
# 改进版滑动窗口
i = 0
j = 0
max_substring_len=0
if len(s) == 0: print(0)
if len(s.strip()) == 0 or len(s) == 1: print(1)
while j < len(s) and i < len(s) - 1:
    if s[j] not in s[i:j]:
        max_substring_len = max(max_substring_len,len(s[i:j+1]))
        j += 1
    else:
        i += 1
print(max_substring_len)