import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = 0

for i in range(N):
    s += min(A)*max(B)
    del A[A.index(min(A))]
    del B[B.index(max(B))]

print(s)