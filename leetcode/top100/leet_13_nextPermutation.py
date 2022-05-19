#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/9 16:43
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_13_nextPermutation.py
@Url     : https://leetcode-cn.com/problems/longest-valid-parentheses/
@Software: PyCharm
"""


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 2: return nums[::-1]

    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            for j in range(len(nums) - 1, i-1, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i + 1:] = nums[i + 1:][::-1]
                    return nums
    return nums[::-1]

print(nextPermutation([1,4,5,2,1,3]))
print([1,2][::-1])
nums=[2,1]
nums[:]=nums[::-1]
print(nums)