#입력
# 4                          // 테스트 케이스의 수
# 4 5                       // N=4, S=5 테스트 케이스 #1
# 4 8 9 10
# 5 7                       // N=5, S=7 테스트 케이스 #2
# 10 4 8 9 1
# 8 1                       // N=8, S=1 테스트 케이스 #3
# 3 5 10 8 9 12 13 15
# 1 2                       // N=1, S=2 테스트 케이스 #4
# 9

#출력
#1 7
#2 12
#3 14
#4 7

from collections import deque
from copy import deepcopy

dx = [-1,1]

def bfs(n,dep,v):
    global ans
    queue = deque()
    queue.append((n,dep,v))

    while queue:
        x,dep,v = queue.popleft()

        if len(v) >= len(arr):
            ans = dep
            return

        for i in range(2):
            nx = x+dx[i]

            if 0<=nx<max(arr)+1:
                if nx in arr:
                    if nx not in v:
                        v2 = deepcopy(v)
                        v2.append(nx)
                        visited[nx] = True
                    queue.append((nx,dep+1,v2))

                elif not visited[nx]:
                    queue.append((nx,dep+1,v))

for t in range(int(input())):
    N,S = map(int,input().split())
    arr = list(map(int, input().split()))
    visited = [False]*(max(arr)+1)
    v = []
    ans = 0

    bfs(S,0,v)

    print(f'#{t+1} {ans}')
    