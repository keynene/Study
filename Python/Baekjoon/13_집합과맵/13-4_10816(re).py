import sys

def bs(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if arr[mid] == target :
        return cnt.get(target)
    elif arr[mid] > target :
        return bs(arr, target, start, mid-1)
    else:
        return bs(arr, target, mid+1, end)

n = int(sys.stdin.readline().rstrip())
num = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().rstrip())
comp = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in num :
    if i in cnt :
        cnt[i] += 1
    else :
        cnt[i] = 1

for i in comp :
    print(bs(num, i, 0, len(num)-1), end=' ')
        



###맞는데 왜 런타임에러###
# import sys

# n = int(sys.stdin.readline().rstrip())
# num = list(map(int, sys.stdin.readline().split()))
# s_num = sorted(num)

# m = int(sys.stdin.readline().rstrip())
# comp = list(map(int, sys.stdin.readline().split()))

# def binary(arr, target, start, end) :
#     cnt = 0

#     mid = (start+end)//2

#     if start > end:
#         return 0
#     elif arr[mid] == target :
#         cnt = num.count(arr[mid])
#         return str(cnt)
#     elif arr[mid] > target :
#         return (binary(arr, target, start, mid-1))
#     else:
#         return (binary(arr, target, start+1, end))


# for i in comp :
#     print(binary(s_num, i, 0, len(num)-1), end=' ')
            





###시간초과(이분탐색사용x)###
# import sys

# n = int(sys.stdin.readline().strip())
# num = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline().strip())
# comp = list(map(int, sys.stdin.readline().split()))

# res = ''
# for i in comp :
#     cnt = 0
#     for j in num :
#         if i == j :
#             cnt += 1
#     res += str(cnt)+' '
# print(res)