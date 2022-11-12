import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(map(int,input().split()))
num = [list(map(int, input().split())) for _ in range(M)]

sumValue = 0
prefix = [0]
for i in arr:
    sumValue += i
    prefix.append(sumValue)

for left, right in num:
    print(prefix[right]-prefix[left-1])


### 시간초과
# import sys
# input = sys.stdin.readline

# N,M = map(int, input().split())
# arr = [0]+list(map(int,input().split()))
# num = [list(map(int, input().split())) for _ in range(M)]

# for s, e in num:
#     ans = 0
#     for i in range(s,e+1):
#         ans  += arr[i]
#     print(ans)