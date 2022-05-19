#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/9 22:28
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_15_search.py
@Url     : 
@Software: PyCharm
"""


def search(nums, target):
    if len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        # 如果左部分有序
        if nums[left] <= nums[mid]:
            if nums[left] == target:
                return left
            # 目标值不在左部有序数组中
            if nums[left] <= target and target<nums[mid]:
                if nums[left] == target: return left
                right = mid - 1
            else:
                left = mid + 1
        # 如果左部分无序，需要做内部判断
        else:
            # 如果小于左部分left，并且大于mid，则数字存在于右部分
            if target <= nums[left] and target > nums[mid]:
                if nums[left] == target: return left
                left = mid + 1
            # 否则数字存在于左部分，继续做二分搜索
            else:
                right = mid - 1
    return -1
nums = [1,3]
target = 3
print(search(nums,target))