import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# n=y m=x
n,m = map(int,input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
next_ice = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[y][x] = True

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<m and 0<=ny<n and ice[ny][nx] != 0 and not visited[ny][nx]:
            dfs(nx,ny)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        visited[y][x] = True
        tcnt = 0

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
                if ice[ny][nx] == 0:
                    tcnt += 1
                else:
                    queue.append((nx,ny))
        next_ice[y][x] = ice[y][x] - tcnt
        if next_ice[y][x] < 0 : next_ice[y][x] = 0

    
time = 1
while True:
    sum_ice = 0
    for y in range(n):
        for x in range(m):
            sum_ice += ice[y][x]
    
    for y in range(n):
        for x in range(m):
            if ice[y][x] != 0 and not visited[y][x]:
                dfs(x,y)
                cnt += 1
    visited = [[False]*m for _ in range(n)]

    if sum_ice == 0 and cnt == 1:
        print(0)
        break

    elif cnt > 1:
        print(time)
        break

    else:
        for y in range(n):
            for x in range(m):
                if ice[y][x] != 0:
                    bfs(x,y)

        for y in range(n):
            for x in range(m):
                ice[y][x] = next_ice[y][x]
        next_ice = [[0]*m for _ in range(n)]
        visited = [[False]*m for _ in range(n)]

        time += 1