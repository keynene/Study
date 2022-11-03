import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int, input().split())
ice = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0

def dfs(x,y):
    ice[y][x] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n and ice[ny][nx] == 0:
            dfs(nx,ny)
            

for y in range(n):
    for x in range(m):
        if not ice[y][x]:
            dfs(x,y)
            cnt += 1
print(cnt)


# #음료수 얼려 먹기

# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# ice = [list(map(int,input().rstrip())) for _ in range(n)]
# res = 0

# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if ice[x][y] == 0:
#         ice[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             res += 1

# print(res)
