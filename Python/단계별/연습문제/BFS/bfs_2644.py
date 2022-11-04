#22:14 #22:55

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
node = [list(map(int, input().split())) for _ in range(m)]

rel = [[] for _ in range(n+1)]  #amap
visited = [False]*(n+1)
res = [0]*(n+1)

for u,v in node:
    rel[u].append(v)
    rel[v].append(u)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        
        for i in rel[v]:
            if not visited[i]:
                queue.append(i)
                res[i] = res[v]+1
                visited[i] = True

bfs(start)
if res[end] > 0:
    print(res[end])
else:
    print(-1)


































# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# for x, y in rel:
#     graph[y][x] = graph[x][y] = 1



# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     visited[x] = True

#     while queue:
#         v = queue.popleft()
        
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if 0<=nx<n+1 and 0<=ny<n+1 and not visited[nx] and graph[ny][nx]==1:




# for y in range(1,n+1):
#     for x in range(1,n+1):
#         if not visited[x] and graph[y][x] == 1:
#             bfs(x,y)