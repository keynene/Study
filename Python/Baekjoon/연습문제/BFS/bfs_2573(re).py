import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melting(cp_ice):
    ice = deepcopy(cp_ice)

    for y in range(n):
        for x in range(m):
            melted = 0
            if cp_ice[y][x] != 0:
                for i in range(4):
                    mx = x+dx[i]
                    my = y+dy[i]
                    if 0<=mx<m and 0<=my<n and ice[my][mx] == 0:
                        melted += 1
                cp_ice[y][x] = cp_ice[y][x]-melted
                if cp_ice[y][x] < 0 : cp_ice[y][x] = 0

    return(cp_ice)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        visited[y][x] = True

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and ice[ny][nx] != 0:
                visited[ny][nx] = True
                queue.append((nx,ny))

year = 0
while True:
    visited = [[False]*m for _ in range(n)]
    sum_ice = sum(map(sum,ice))
    cnt = 0

    if sum_ice == 0:
        print(0)
        break
    
    for y in range(n):
        for x in range(m):
            if ice[y][x] != 0 and not visited[y][x]:
                bfs(x,y)
                cnt += 1

    if cnt > 1:
        print(year)
        break
    else:
        ice = melting(ice)
        year += 1



##현진이 풀이 (reduce함수로 매개변수로 ice 녹이기)
# import collections
# from copy import deepcopy


# n, m = map(int, input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
# dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


# def reduce (graph2) :

#     graph = deepcopy(graph2)
    
#     for i in range(n) :
#         for j in range(m) :
#             if graph2[i][j] != 0 :
#                 for tx , ty in zip(dx , dy) :
#                     if n > ty + i >=0 and m > tx + j >=0 and graph[ty + i][tx + j] == 0 :
#                         if graph2[i][j] == 0 :
#                             break;
#                         graph2[i][j] = graph2[i][j]-1;

#     return graph2
    
# def bfs (graph) :
    
#     visite = [[False] * m for _ in range(n) ]
    
#     count = 0;
#     queue = collections.deque()
#     for i in range(n) :
#         for j in range(m) :
#             if graph[i][j] != 0 and not visite[i][j]:
#                 queue.append((i,j))
#                 visite[i][j] = True
#                 while queue :
#                     y , x = queue.popleft()
#                     for tx , ty in zip(dx , dy) :
#                         ny = ty + y
#                         nx = tx + x
#                         if n > ny >=0 and m > nx >=0 and graph[ny][nx] != 0 and not visite[ny][nx]:
#                             queue.append( (ny , nx) )
#                             visite[ny][nx] = True
#                 count = count +1
    
#     if count >= 2 :
#         return True
#     else : 
#         return False
    
# year = 0;    
    
# while True :
#     if bfs(graph) :
#         print(year)
#         break;
    
#     graph = reduce(graph)
#     year = year+1
