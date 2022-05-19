#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/5 16:14
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_8_letter_combinations.py
@Url     : https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
@Software: PyCharm
"""

# nums = [2,3,3,4,5,6]
#
# for i in range(len(nums)):
#     print(nums.pop())

def letterCombinations(digits):

    # """
    # 		:type digits: str
    # 		:rtype: List[str]
    # 		"""
    # # 注意边界条件
    # if not digits:
    #     return []
    # # 一个映射表，第二个位置是"abc“,第三个位置是"def"。。。
    # # 这里也可以用map，用数组可以更节省点内存
    # d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    # # 最终输出结果的list
    # res = []
    #
    # # 递归函数
    # def dfs(tmp, index):
    #     # 递归的终止条件，注意这里的终止条件看上去跟动态演示图有些不同，主要是做了点优化
    #     # 动态图中是每次截取字符串的一部分，"234"，变成"23"，再变成"3"，最后变成""，这样性能不佳
    #     # 而用index记录每次遍历到字符串的位置，这样性能更好
    #     if index == len(digits):
    #         res.append(tmp)
    #         return
    #     # 获取index位置的字符，假设输入的字符是"234"
    #     # 第一次递归时index为0所以c=2，第二次index为1所以c=3，第三次c=4
    #     # subString每次都会生成新的字符串，而index则是取当前的一个字符，所以效率更高一点
    #     c = digits[index]
    #     # map_string的下表是从0开始一直到9， ord(c)-48 是获取c的ASCII码然后-48,48是0的ASCII
    #     # 比如c=2时候，2-'0'，获取下标为2,letter_map[2]就是"abc"
    #     letters = d[ord(c) - 48]
    #
    #     # 遍历字符串，比如第一次得到的是2，页就是遍历"abc"
    #     for i in letters:
    #         # 调用下一层递归，用文字很难描述，请配合动态图理解
    #         dfs(tmp + i, index + 1)
    #
    # dfs("", 0)
    # return res
    #  2. 队列拼接法
    if len(digits) == 0: return []
    map_string = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    res = ['']
    for i in digits:
        chars = map_string[i]
        size = len(res)

        for _ in range(size):
            tmp = res.pop(0)
            for char in chars:
                res.append(tmp + char)
    return res
    # 3. dfs 回溯算法
    # char_comb_list = []
    # res_comb_list = []
    # def dfs(ind):
    #     if ind == len(digits): return res_comb_list.append(''.join(char_comb_list))
    #
    #     chars = map_string[digits[ind]]
    #     for char in chars:
    #         char_comb_list.append(char)
    #         dfs(ind + 1)
    #         char_comb_list.pop()
    #
    # dfs(0)
    # return res_comb_list

letterCombinations("232")