#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 10:56
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_1_two_nums_sum.py
@url     : https://leetcode-cn.com/problems/two-sum/
@Software: PyCharm
"""
# 1. 暴力求解，循环遍历两次数组，最大时间复杂度：O(n2),空间复杂度：O(1)

nums = [1, 3, 11, 15, 2, 7]
target = 9

is_find_result = False
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            is_find_result = True
            break
    if is_find_result:
        break

# 2. 哈希表 最大时间复杂度：O(n),空间复杂度：O(n)

# 创建哈希表，即dict
hash_index = dict()
for i,j in enumerate(nums):
    if target - j in hash_index.keys():
        print([i, hash_index[target-j]])
        break
    hash_index[j] = i
    # print(hash_index)

hash_index = dict()
for i in range(len(nums)):
    if target - nums[i] in hash_index.keys():
        print([i, hash_index[target-nums[i]]])
        break
    hash_index[nums[i]] = i
    # print(hash_index)
