import sys
input = sys.stdin.readline

maxR = -1e9
minR = 1e9

def dfs(idx, res, sum, sub, mul, div):
    global maxR, minR

    if idx == n:
        maxR = max(res, maxR)
        minR = min(res, minR)
        return

    if sum:
        dfs(idx+1, res+a[idx], sum-1, sub, mul, div)
    if sub:
        dfs(idx+1, res-a[idx], sum, sub-1, mul, div)
    if mul:
        dfs(idx+1, res*a[idx], sum, sub, mul-1, div)
    if div:
        dfs(idx+1, int(res/a[idx]), sum, sub, mul, div-1)

n = int(input().rstrip())
a = list(map(int, input().split()))
f = list(map(int, input().split()))


dfs(1, a[0], f[0], f[1], f[2], f[3])
print(maxR)
print(minR)




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
