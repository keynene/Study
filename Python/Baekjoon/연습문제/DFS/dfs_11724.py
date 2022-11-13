import sys
input = sys.stdin.readline

n,m = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
amap = [[] for _ in range(n+1)]

for u,v in node:
    amap[u].append(v)
    amap[v].append(u)

cnt = 0
visited = [0]*(n+1)
def dfs(v):
    visited[v] = 1
    for i in amap[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)






# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# node = [list(map(int, input().split())) for _ in range(m)]
# amap = [[] for _ in range(n+1)]
# visited = [0 for _ in range(n+1)]

# for x, y in node:
#     amap[x].append(y)
#     amap[y].append(x)

# cnt = 0

# def dfs(v):
#     visited[v] = 1
#     for i in amap[v]:
#         if not visited[i]:
#             dfs(i)

# for i in range(1, n+1):
#     if not visited[i]:
#         dfs(i)
#         cnt += 1

# print(cnt)