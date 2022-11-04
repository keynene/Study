#약 00:00  #1:50
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,1,-1,-1]
dy = [1,-1,1,-1]

def bfs():
    global cnt
    queue = deque()
    queue.append((sx,sy,cnt))
    
    while queue:
        x,y,dep = queue.popleft()

        if x==ex and y==ey:
            print(chess[y][x])
            return

        for i in range(4):
            nx = x+2*dx[i]
            ny = y+1*dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if chess[ny][nx] == 0:
                    chess[ny][nx] = dep+1
                    queue.append((nx,ny,chess[ny][nx]))

                if chess[nx][ny] == 0:
                    chess[nx][ny] = dep+1
                    queue.append((ny,nx,chess[nx][ny]))

for i in range(int(input())):
    n = int(input())
    cnt = 0
    chess = [[0 for _ in range(n)] for _ in range(n)]
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    bfs()