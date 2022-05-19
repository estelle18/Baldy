#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/10 16:52
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_17_CombinationNums.py
@Url     : 
@Software: PyCharm
"""

def combinationSum(candidates,target):
    candidates.sort()
    ans = []
    def dfs(candidates,may_coms,target):
        if len(candidates) == 0: return
        if candidates[0] > target: return
        if candidates[0] == target:
            ans.append(may_coms+[target])
            return
        dfs(candidates,may_coms+candidates[0:1],target-candidates[0])
        dfs(candidates[1:],may_coms,target)
    dfs(candidates,[],target)
    return ans

print(combinationSum([2,3,6,7],7))


def permute(nums):
    if len(nums) == 0: return [nums]
    ans = []

    def dfs(remaind_nums, current_comb):
        if len(remaind_nums) == 0:
            ans.append(current_comb)
            return
        for i in range(len(remaind_nums)):
            # remaind 去掉当前选择的元素
            dfs(remaind_nums[:i] + remaind_nums[i + 1:], current_comb + [remaind_nums[i]])

    dfs(nums,[])
    return ans

print(permute([1,2,3]))