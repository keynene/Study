import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
matrix = [[0]*(n+1) for _ in range(n+1)] #인접행렬

for x,y in node:
    matrix[y][x] = matrix[x][y] = 1

d_visited = [False]*(n+1)
def dfs(v):
    print(v, end=' ')
    d_visited[v] = True

    for i in range(1, n+1):
        if not d_visited[i] and matrix[v][i]:
            dfs(i)


b_visited = [False]*(n+1)
def bfs(v):
    queue = deque([v])
    b_visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if not b_visited[i] and matrix[v][i] == 1:
                queue.append(i)
                b_visited[i] = True

dfs(v)
print()
bfs(v)


#DFS 내풀이 + BFS 다른사람풀이 
# n,m,v = map(int, input().split())
# node = [list(map(int, input().split())) for _ in range(m)]
# amap = [[] for _ in range(n+1)]

# #amap에 매핑
# for x,y in node:
#     amap[x].append(y)
#     amap[y].append(x)

# for i in range(1,n+1):
#     amap[i].sort()

# #DFS
# d_visited = [False]*(n+1)
# def dfs(v):
#     print(v, end=' ')
#     d_visited[v] = True
#     for i in amap[v]:
#         if not d_visited[i]:
#             dfs(i)

# #BFS
# b_visited = [False]*(n+1)
# def bfs(v):
#     queue = deque([v])
#     b_visited[v] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in amap[v]:
#             if not b_visited[i]:
#                 queue.append(i)
#                 b_visited[i] = True

# dfs(v)
# print()
# bfs(v)