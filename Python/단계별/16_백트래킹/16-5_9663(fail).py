#22:10
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
chess = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dep = 0
cnt = 0

def dfs(x,y):
    global cnt
    visited[y][x] = True
    for i in range(1,n):
        for j in range(8):
            dx = [i,i,0,-i,-i,-i,0,i]
            dy = [0,i,i,i,0,-i,-i,-i]
            nx = x+dx[j]
            ny = y+dy[j]

            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                visited[ny][nx] = True
    print(visited)
    return

dfs(0,0)