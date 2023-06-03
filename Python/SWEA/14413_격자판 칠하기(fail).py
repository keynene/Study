from collections import deque

dx = [1,1,-1,-1]
dy = [-1,1,1,-1]

cx = [-1,1,0,0]
cy = [0,0,-1,1]

def bfs(x,y):
  global ans
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      mx = x+cx[i]
      my = y+cy[i]
      if 0<=mx<M and 0<=my<N and graph[my][mx] == graph[y][x]:
        ans = 'impossible'
        return

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<M and 0<=ny<N:
        if graph[ny][nx] == '?':
          graph[ny][nx] = graph[y][x]
          queue.append((nx,ny))
        elif graph[ny][nx] != graph[y][x]:
          ans = 'impossible'
          return


for T in range(int(input())):
  N,M = map(int, input().split())
  graph = [list(map(str,input().rstrip())) for _ in range(N)]
  mode = []
  ans = 'possible'

  for y in range(N):
    for x in range(M):
      if graph[y][x] != '?':
        bfs(x,y)
    if ans == 'impossible':
      break
  
  print(graph)
  print(f'#{T+1} {ans}')

