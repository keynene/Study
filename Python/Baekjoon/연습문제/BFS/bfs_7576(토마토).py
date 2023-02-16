import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
toma = [list(map(int,input().split())) for _ in range(N)]
tomato = []
isErr = False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr):
	queue = deque()
	
	for x,y in arr:
		queue.append((x,y))

	while queue:
		x,y = queue.popleft()

		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]

			if 0<=nx<M and 0<=ny<N and toma[ny][nx] == 0:
				toma[ny][nx] = toma[y][x] + 1
				queue.append((nx,ny))


for y in range(N):
	for x in range(M):
		if toma[y][x] == 1:
			tomato.append([x,y])

bfs(tomato)

for y in range(N):
	for x in range(M):
		if toma[y][x] == 0:
			isErr = True

if isErr:
	print(-1)
else:
	print(max(map(max,toma))-1)