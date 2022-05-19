#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/1 22:07
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_6_maxArea.py
@Url     : https://leetcode-cn.com/problems/container-with-most-water/
@Software: PyCharm
"""
h= [1,8,6,2,5,4,8,3,7]
def maxArea( height):
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < len(height) - 1 and j > i:
        max_area = max(0,abs(i - j) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

print(maxArea(h))
