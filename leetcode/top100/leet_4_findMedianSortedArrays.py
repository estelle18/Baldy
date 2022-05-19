#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 17:45
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_4_findMedianSortedArrays.py
@Url     : https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
@Software: PyCharm
"""

nums1 = [1,3]
nums2 = [2]


# def findMedianSortedArrays( nums1, nums2) :
#     m = len(nums1)
#     n = len(nums2)
#     if m == 0 and n == 0: return 0
#     # 提前退出条件：够取中位数足以
#     odd_index = (m + n) // 2
#     is_odd_flag = True if  (m + n) % 2 != 0 else False
#     i = 0
#     j = 0
#     new_list = []
#     while i < m and j < n and len(new_list) <= odd_index+1:
#         if nums1[i] <= nums2[j]:
#             new_list.append(nums1[i])
#             i += 1
#         else:
#             new_list.append(nums2[j])
#             j += 1
#     if i < m: new_list.extend(nums1[i:])
#     if j < n: new_list.extend(nums2[j:])
#     if is_odd_flag:
#         return new_list[odd_index]
#     else:
#         return (new_list[odd_index] + new_list[odd_index - 1]) / 2

def findMedianSortedArrays( nums1, nums2) :
    def getKthElement(k):
        """
        - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
        - 这里的 "/" 表示整除
        - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        - 这样 pivot 本身最大也只能是第 k-1 小的元素
        - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
        """

        index1, index2 = 0, 0
        while True:
            # 特殊情况
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # 正常情况
            newIndex1 = min(index1 + k // 2 - 1, m - 1)
            newIndex2 = min(index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1

    m, n = len(nums1), len(nums2)
    totalLength = m + n
    if totalLength % 2 == 1:
        return getKthElement((totalLength + 1) // 2)
    else:
        return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


print(findMedianSortedArrays(nums1,nums2))