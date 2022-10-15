import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = set(input().rstrip() for _ in range(n))
comp = list(input().rstrip() for _ in range(m))

cnt = 0
for comp_str in comp:
    if comp_str in S:
        cnt += 1
print(cnt)

#다른풀이
#list 없이 해결하기

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = set(input().rstrip() for _ in range(n))

cnt = 0
for _ in range(m):
    comp = input().rstrip()
    if comp in S:
        cnt += 1
print(cnt)