import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
node = [list(map(int, input().split())) for _ in range(m)]
cmap = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for u,v in node:
    cmap[u].append(v)
    cmap[v].append(u)

def dfs(v):
    global cnt
    for i in cmap[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

for i in cmap[1]:
    if not visited[i]:
        visited[i] = 1
        dfs(i)
dfs(1)
print(sum(visited)-1)