#음료수 얼려 먹기

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ice = [list(map(int,input().rstrip())) for _ in range(n)]
res = 0

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            res += 1

print(res)
