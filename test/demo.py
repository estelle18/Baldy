import sys
dependency_list = list(map(str,sys.stdin.readline().strip().split(',')))
fail_list = set(map(str, sys.stdin.readline().strip().split(',')))
# 所有服务集合
serve_list = []
serve_pair = []
for dep in dependency_list:
    dep_pair = dep.split('-')
    for i in dep_pair:
        if i not in serve_list:
            serve_list.append(i)
    serve_pair.append(dep_pair)

# 根据故障服务删除依赖其的服务
for depend_pair in serve_pair:
    if depend_pair[1] in fail_list and depend_pair[0] in serve_list:
        serve_list.remove(depend_pair[0])
        fail_list.add(depend_pair[0])
# 删除故障服务：
for fail_serve in fail_list:
    if fail_serve in serve_list:
        serve_list.remove(fail_serve)
serve_list=[]
print(','.join(serve_list))


# import sys
# input_str = list(map(int, sys.stdin.readline().strip().split(',')))
#
# # 找到连续0最多的序列
# # 三种情况：从左往右开始连续0，中间两个1夹一串0，从右往左开始一串0
#
# max_long_nums = 0
# mid_nums = 0
# left_nums = 0
# right_nums = 0
#
# if input_str[0] == 0:
#     for i in input_str:
#         if i == 0:
#             left_nums += 1
#         else:
#             break
# if input_str[-1] == 0:
#     for i in input_str[::-1]:
#         if i == 0:
#             right_nums += 1
#         else:
#             break
# for i in range(left_nums+1,len(input_str)-(right_nums+1)):
#     if input_str[i] == 0:
#         mid_nums += 1
#         max_long_nums = max(max_long_nums, mid_nums)
#     else:
#         mid_nums = 0
#
# if max_long_nums % 2 == 0:
#     max_long_nums = max_long_nums // 2
# else:
#     max_long_nums = max_long_nums // 2 + 1
#
# print(max(max_long_nums,left_nums,right_nums))



import sys

# input_str = 'mMbccbc'
#
# # 特殊情况判断
# if input_str.isalpha():
#     print(0)
#
#
# # 使用栈做栈顶元素与待匹配元素比较
# res = []
# for i in input_str:
#     if not res:
#         res.append(i)
#     else:
#         if res[-1] == i:
#             res.pop()
# print(len(res))
# def re_search(i, j, s, res_len):
#     if i >= len(s) or j >= len(s):
#         return i, j, res_len
#     i -= 1
#     j += 1
#     if s[i] != s[j]:
#         i = j
#         j += 1
#     else:
#         res_len -= 2
#         if res_len >= 2:
#             re_search(i, j, s, res_len)
#     return i, j, res_len
#
#
# i = 0
# j = 1
# res_len = len(input_str)
# while (j < len(input_str) and i < len(input_str)) or res_len!= 0:
#     if input_str[i] != input_str[j]:
#         i += 1
#         j += 1
#     else:
#         res_len -= 2
#         if res_len >= 2:
#             re_search(i, j, input_str, res_len)
# print(res_len)