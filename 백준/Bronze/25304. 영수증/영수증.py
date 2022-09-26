import sys
import math
X = int(input())
N = int(input())
C = [0]*N
plus = 0;
for i in range(N):
    C[i] = math.prod(map(int,sys.stdin.readline().split()))
    plus = plus + C[i];
if X == plus:
    print('Yes')
else:
    print('No')