import sys

T = int(input())
C = [0]*T
for i in range(T):
    C[i] = sum(map(int,sys.stdin.readline().split()))
for i in range(T):
    print(C[i])