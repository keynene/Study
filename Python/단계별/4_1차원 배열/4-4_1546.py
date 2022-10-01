from audioop import avg
import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = max(arr)
for i in range(N):
    arr[i] = arr[i]/M*100
print(sum(arr)/N)
