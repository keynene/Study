#22:23

import sys
input = sys.stdin.readline

N,K = map(int, input().split())
buy = 0

while bin(N).count('1') > K:
    N += 1
    buy += 1

print(buy)
    



##틀림
# import sys
# input = sys.stdin.readline

# N,K = map(int, input().split())
# bottle_cnt = 0

# def bottle(N,dep):
#     global bottle_cnt

#     if N == K:
#         print(bottle_cnt)
#         return
#     elif N < K:
#         sub = K-N
#         bottle_cnt += (2**dep)*sub
#         print(bottle_cnt)
#         return
#     else:
#         if N%2 != 0:
#             N += 1
#             bottle_cnt += 2**dep
        
#         N = N//2
#         bottle(N,dep+1)

# bottle(N,0)

