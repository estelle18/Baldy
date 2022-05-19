#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 21:36
@Author  : estelle.ji
@Email   : mingshu.ji@amh-group.com
@File    : leet_5_longestPalindrome.py
@Url     : https://leetcode-cn.com/problems/longest-palindromic-substring/
@Software: PyCharm
"""
import time
import numpy as np
s = "babad"

# 判断当前字符串是否为回文串
def isPalindromeStr(s):
    if len(s) < 2: return True
    if len(s) == 2: return s[0] == s[1]

    # 从中间位置对半分，比较数值是否一致,不一致则返回不是回文串
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


# 1. 暴力求解
# def longestPalindrome(s):
#     max_string_len = 0
#     result_string = ""
#     # 特殊情况处理：
#     #   字符串长度为1，一定为回文字串；
#     #   长度为2，如果两个字符一致则为回文子串
#     n = len(s)
#     if n < 2: return s
#     if n == 2 and s[0] == s[1]: return s
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             current_str = s[i:j + 1]
#             if isPalindromeStr(current_str) and len(current_str)>max_string_len:
#                 max_string_len = len(current_str)
#                 result_string = current_str
#     return result_string

# 2. 优化版暴力求解——动态规划
def longestPalindrome(s):
    start = time.clock()
    if len(s) < 2: return s
    if len(s) == 2 and s[0] == s[1]: return s
    max_string_len = 0
    result_string = ""
    # 动态规划，先初始化dp矩阵,dp[i,j]表示字符串s[i:j]是回文子串
    dp = [[False] * len(s) for _ in range(len(s))]
    # 遍历所有可能回文串的长度
    for i in range(1,len(s)+1):
        for left in range(len(s)):
            right = left+i-1
            if (right >= len(s)): break
            dp[left][right] = (i==1) or (i==2 and s[left]==s[right]) or (dp[left+1][right-1] and s[left]==s[right])
            if (dp[left][right] and i>max_string_len):
                max_string_len = i
                result_string = s[left:right+1]
    end = time.clock()
    print("运行耗时(ms)", (end - start)*1000)
    return result_string

s="reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye"


# 3. 最长公共子串法【连续】
def longestPalindrome2(s):
    # 特殊情况处理：
    if s == '': return s
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    s2 = s[::-1]
    max_len = 0
    max_end = 0
    for i in range(n):
        for j in range(n):
            if s[i] == s2[j]:
                if (i == 0) or (j == 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1

            if dp[i][j] > max_len:
                max_len = dp[i][j]
                max_end = i
    return s[max_end - max_len + 1:max_end + 1]

print(longestPalindrome2("aacabdkacaa"))

