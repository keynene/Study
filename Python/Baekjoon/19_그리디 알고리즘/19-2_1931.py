import sys
input = sys.stdin.readline

n = int(input())
conf = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:(x[1],x[0]))
cnt = 0
last = 0

for time in conf:
    if time[0] >= last:
        cnt += 1
        last = time[1]
print(cnt)