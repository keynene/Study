import sys
input = sys.stdin.readline

N,M = map(int, input().split())
name = [input().rstrip() for _ in range(N)]
time = sorted([list(map(str, input().split())) for _ in range(M)], key=lambda x:(x[0],x[1]))

print(*time,sep="\n")