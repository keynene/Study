import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[y][x] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and amap[y][x] == amap[ny][nx] and not visited[ny][nx]:
            dfs(nx,ny)

n = int(input().rstrip())
amap = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
acnt = 0

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y)
            acnt += 1

for y in range(n):
    for x in range(n):
        if amap[y][x] == 'R':
            amap[y][x] = 'G'

rgcnt = 0
visited = [[False]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(x,y)
            rgcnt += 1

print(acnt, rgcnt)


#두 번째 풀이
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# n = int(input().rstrip())
# rgb = [list(map(str, input().rstrip())) for _ in range(n)]
# amap = []
# visited = [[0 for _ in range(n)] for _ in range(n)]
# cnt = 0
# res = []

# def dfs(x,y,num):
#     if x<0 or y<0 or x>=n or y>=n:
#         return
#     if visited[y][x] == 1 or amap[y][x] != num:
#         return
#     elif amap[y][x] == num:
#         visited[y][x] = 1
#         if num == 2:
#             amap[y][x] = 0
#         dfs(x-1,y,num)
#         dfs(x,y-1,num)
#         dfs(x+1,y,num)
#         dfs(x,y+1,num)
#         return
    
# for string in rgb:
#     num = ''
#     for al in string:
#         if al == 'R':
#             num += str(0)+' '
#         elif al == 'B':
#             num += str(1)+' '
#         elif al == 'G':
#             num += str(2)+' '
#     amap.append(list(map(int, num.split())))

# for y in range(n):
#     for x in range(n):
#         if not visited[y][x]:
#             dfs(x,y,amap[y][x])
#             cnt += 1
# res.append(cnt)

# cnt = 0
# visited = [[0 for _ in range(n)] for _ in range(n)]
# for y in range(n):
#     for x in range(n):
#         if not visited[y][x]:
#             dfs(x,y,amap[y][x])
#             cnt += 1
# res.append(cnt)
# print(*res)


#12:48 #1:33 #첫번째 풀이
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# n = int(input().rstrip())
# graph = [list(input().rstrip()) for _ in range(n)]
# amap = []
# rgmap = []
# acnt = 0
# rgcnt = 0

# def dfs(x,y,map,num):
#     if x<0 or y<0 or x>=n or y>=n:
#         return
#     if map[y][x] == 3 and map[y][x] != num:
#         return
#     elif map[y][x] == num:
#         map[y][x] = 3
#         dfs(x-1,y,map,num)
#         dfs(x,y-1,map,num)
#         dfs(x+1,y,map,num)
#         dfs(x,y+1,map,num)
#         return
#     else:
#         return

# for rgb in graph:
#     string = 0
#     num = ''
#     rgnum = ''
#     for string in rgb:
#         if string == 'R':
#             num += str(0)+' '
#             rgnum += str(0)+' '
#         elif string == 'B':
#             num += str(1)+' '
#             rgnum += str(1)+' '
#         elif string == 'G':
#             num += str(2)+' '
#             rgnum += str(0)+' '
#     amap.append(list(map(int, num.split())))
#     rgmap.append(list(map(int, rgnum.split())))

# for y in range(n):
#     for x in range(n):
#         if amap[y][x] != 3:
#             dfs(x,y,amap,amap[y][x])
#             acnt += 1
#         if rgmap[y][x] != 3:
#             dfs(x,y,rgmap,rgmap[y][x])
#             rgcnt += 1

# print(acnt, rgcnt, sep=' ')
        