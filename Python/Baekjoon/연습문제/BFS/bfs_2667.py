import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    house[y][x] = 0
    dep = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N and house[ny][nx] == 1:
                house[ny][nx] = 0
                dep += 1
                queue.append((nx,ny))

    return dep

acnt = 0
hcnt = []
for y in range(N):
    for x in range(N):
        if house[y][x] == 1:
            hcnt.append(bfs(x,y))
            acnt += 1

print(acnt,*sorted(hcnt),sep="\n")