#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/10 14:55
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_16_searchRange.py
@Url     : https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
@Software: PyCharm
"""
def searchRange(nums,target):
    if len(nums) == 0: return [-1,-1]
    if len(nums) == 1:
        if nums[0] != target:
            return [-1,-1]
        else:
            return[0,0]

    # 分为两步，先找首位，再找末位
    # 1. 找首位
    def first_position(nums,target):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if nums[left] == target: return left
        return -1
    # 2. 找末位
    def last_position(nums,target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return left

    # 找首位都没找到，说明该nums中不包含target，直接返回【-1，-1】
    min_index = first_position(nums,target)
    if min_index == -1: return [-1,-1]
    max_index = last_position(nums,target)
    return [min_index,max_index]


print(searchRange([5,7,8,8,8,10],8))