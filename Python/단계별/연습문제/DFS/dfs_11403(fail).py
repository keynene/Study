import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = []
ans = set()

def dfs(x,y):
    global result
    visited[y][x] = True
    if x not in cycle:
        cycle.append(x)
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and graph[ny][nx]:
            dfs(nx,ny)
        if 0<=nx<n and 0<=ny<n and visited[ny][nx]:
            if nx in cycle and nx not in result:
                result += cycle[cycle.index(nx):]

for y in range(n):
    for x in range(n):
        if graph[y][x]:
            graph[x][y] = 1

for y in range(n):
    for x in range(n):
        if not visited[y][x] and graph[y][x]:
            cycle = []
            dfs(x,y)
            for i in result:
                graph[i][i] = 1
                visited[i][i] = True
            result = []
print(*graph,sep="\n")

