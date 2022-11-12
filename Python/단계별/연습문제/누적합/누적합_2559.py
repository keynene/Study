import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = list(map(int, input().split()))

p = []
p.append(sum(arr[:K]))

for i in range(N-K):
    p.append(p[i] - arr[i] + arr[K+i])
        
print(max(p))






# import sys
# input = sys.stdin.readline

# N,K = map(int,input().split())
# arr = list(map(int,input().split()))
# p = [0]

# sumValue = 0
# cnt = 0
# idx = 0
# for i in range(N):
#     cnt += 1
#     sumValue += arr[i]
#     if cnt == K:
#         p.append(sumValue)
#         sumValue -= arr[idx]
#         idx += 1
#         cnt -= 1
# del p[0]
# print(max(p))