import sys
input = sys.stdin.readline

n,m = map(int, input().split())
root = [list(map(int,input().rstrip())) for _ in range(n)]


def bfs(x,y,cnt):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return cnt
    if root[x][y] == 1:
        cnt += 1
        root[x][y] = 0
        bfs(x-1, y,cnt)
        bfs(x, y-1,cnt)
        bfs(x+1, y,cnt)
        bfs(x, y+1,cnt)


    if x == n-1 and y == m-1:
        return print(cnt)
    return cnt

for i in range(n):
    for j in range()
