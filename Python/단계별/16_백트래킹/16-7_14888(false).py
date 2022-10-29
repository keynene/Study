






















import sys
input = sys.stdin.readline

maxR = -1e9
minR = 1e9

def dfs(idx, res, sum, sub, mul, div):
    global maxR
    global minR

    if idx == n-1:
        maxR = max(res, maxR)
        minR = min(res, minR)
        return [maxR, minR]

    if sum:
        dfs(idx+1, res+a[idx+1], sum-1, sub, mul, div)
    if sub:
        dfs(idx+1, res-a[idx+1], sum, sub-1, mul, div)
    if mul:
        dfs(idx+1, res*a[idx+1], sum, sub, mul-1, div)
    if div:
        if res < 0:
            res *= -1
        dfs(idx+1, res//a[idx+1], sum, sub, mul, div-1)

n = int(input().rstrip())
a = list(map(int, input().split()))
f = list(map(int, input().split()))


want = dfs(0, a[0], f[0], f[1], f[2], f[3])
print(want)
# print(maxR)
# print(minR)

















































# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# num = list(map(int, input().split()))
# f = list(map(int, input().split()))

# maxN = -1e9
# minN = 1e9

# def dfs(idx, total, pl, mi, mul, div):
#     global maxN, minN
#     if idx == n:
#         maxN = max(total, maxN)
#         minN = min(total, minN)
#         return

#     if pl:
#         dfs(idx+1, total+num[idx], pl-1, mi, mul,div)
#     if mi:
#         dfs(idx+1, total-num[idx], pl, mi-1, mul,div)
#     if mul:
#         dfs(idx+1, total*num[idx], pl, mi, mul-1,div)
#     if div:
#         if total < 0:
#             total *= -1
#         dfs(idx+1, total//num[idx], pl, mi, mul,div-1)

# dfs(1, num[0], f[0], f[1], f[2], f[3])
# print(maxN)
# print(minN)









# #이해안가는 알고리즘 1
# # import sys
# # input = sys.stdin.readline

# # n = int(input().rstrip())
# # number = list(map(int, input().split()))
# # f = list(map(int, input().split()))
# # minN = 1e9
# # maxN = -1e9
# # ans = number[0]

# # def dfs(idx):
# #     global ans
# #     global minN, maxN

# #     if idx == n:
# #         if ans > maxN:
# #             maxN = ans
# #         elif ans < minN:
# #             minN = ans
# #         return
    
# #     for i in range(4):
# #         tmp = ans
# #         if f[i] > 0:
# #             if i == 0:
# #                 ans += number[idx]
# #             elif i == 1:
# #                 ans -= number[idx]
# #             elif i == 2:
# #                 ans *= number[idx]
# #             else:
# #                 if ans < 0:
# #                     ans *= -1
# #                 ans = ans//number[idx]
            
# #             f[i] -= 1
# #             dfs(idx+1)
# #             ans = tmp
# #             f[i] += 1
# # dfs(1)
# # print(maxN)
# # print(minN)








# # 내알고리즘...
# # import sys
# # input = sys.stdin.readline

# # n = int(input().rstrip())
# # a = list(map(int, input().split()))
# # plus, minus, mul, div = map(int, input().split())

# # max_list = [minus, div, plus, mul] #1,1,2,1
# # min_list = [plus, div, minus, mul]

# # res_max = []
# # res_min = []

# # for i in a:
# #     res_max.append(i)
# #     res_min.append(i)


# # def a_max(num):
# #     while len(num) > 1:
# #         for i in range(len(num)-1):
# #             if max_list[0] != 0:
# #                 num[i] = num[i] - num[i+1]
# #                 max_list[0] -= 1

# #             elif max_list[1] != 0:
# #                 if num[i] < 0:
# #                     num[i] *= -1
# #                 num[i] = num[i] // num[i+1]
# #                 max_list[1] -= 1

# #             elif max_list[2] != 0:
# #                 num[i] = num[i] + num[i+1]
# #                 max_list[2] -= 1
            
# #             elif max_list[3] != 0:
# #                 num[i] = num[i] * num[i+1]
# #                 max_list[3] -= 1
# #             del num[i+1]
# #             break
# #     return num
# # print(a_max(res_max))

# # def a_min(num):
# #     while len(num) > 1:
# #         for i in range(len(num)-1):
# #             if min_list[0] != 0:
# #                 num[i] = num[i] + num[i+1]
# #                 min_list[0] -= 1

# #             elif min_list[1] != 0:
# #                 if num[i] < 0:
# #                     num[i] *= -1
# #                 num[i] = num[i] // num[i+1]
# #                 min_list[1] -= 1
            
# #             elif min_list[2] != 0:
# #                 num[i] = num[i] - num[i+1]
# #                 min_list[2] -= 1

# #             elif min_list[3] != 0:
# #                 num[i] = num[i] * num[i+1]
# #                 min_list[3] -= 1
# #             del num[i+1]
# #             break
# #     return num
# # print(a_min(res_min))
