#21:19

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

p = []
mul = 1
ans = []

for i in range(N):
    mul *= arr[i]
    p.append(mul)

for i in range(1,len(p)):
    
