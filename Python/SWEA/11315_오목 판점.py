def move(arr):
    global ans
    dx = [0,1,1,1]
    dy = [1,1,0,-1]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                for i in range(4):
                    ny = y
                    nx = x
                    cnt = 0
                    while 0<=ny<N and 0<=nx<N and arr[ny][nx]=='o':
                        cnt += 1
                        nx += dx[i]
                        ny += dy[i]
                    if cnt >=5:
                        ans = 'YES'
                        return 
    return 

for t in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'NO'

    move(arr)

    print(f'#{t+1} {ans}')



# def move(arr):
#     global ans
#     dr = [0,1,1,1]
#     dc = [1,0,1,-1]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'o':
#                 for d in range(4):
#                     r = i
#                     c = j
#                     cnt = 0
#                     while 0<=r<N and 0<=c<N and arr[r][c]=='o':
#                         cnt += 1
#                         r += dr[d]
#                         c += dc[d]
#                     if cnt >=5:
#                         ans = 'YES'
#                         return 
#     return 

# for t in range(int(input())):
#     N = int(input())
#     arr = [input() for _ in range(N)]
#     ans = 'NO'

#     move(arr)

#     print(f'#{t+1} {ans}')





# from collections import deque



# def bfs(x,y):
#     global ans
#     queue = deque()
#     queue.append((x,y,1))

#     while queue:
#         x,y,dep = queue.popleft()

#         if dep == 5:
#             ans = 'YES'
#             return
        
#         for i in range(5):
#             dx = [-1,0,1,1]
#             dy = [-1,-1,-1,0]
#             for j in range(4):
#                 nx = x+dx[j]
#                 ny = y+dy[j]

#                 if 0<=nx<N and 0<=ny<N and arr[ny][nx] == 'o':
#                     queue.append((nx,ny,dep+1))

# for t in range(int(input())):
#     N = int(input())
#     arr = [list(map(str, str(input()))) for _ in range(N)]
#     ans = 'NO'

#     for y in range(N):
#         for x in range(N):
#             if arr[y][x] == 'o':
#                 bfs(x,y)
#     print(*arr,sep="\n")

#     print(f'#{t+1} {ans}')