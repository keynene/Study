<<<<<<< HEAD
# dx = [-1,0,1,1]
# dy = [1,1,1,0]

=======
dx = [-1,0,1,1]
dy = [1,1,1,0]

def dfs(x,y):
    global ans
    for i in range(4):
        nx = x
        ny = y
        cnt = 0
        while 0<=nx<N and 0<=ny<N and arr[ny][nx]=='o':
            cnt += 1
            nx += dx[i]
            ny += dy[i]
        if cnt >= 5:
            ans = 'YES'
            return

for t in range(int(input())):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    ans = 'NO'

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                dfs(x,y)

    print(f'#{t+1} {ans}')



































# dx = [-1,0,1,1]
# dy = [1,1,1,0]

>>>>>>> origin/master
# def dfs(x,y):
#     global ans
#     for i in range(4):
#         nx = x
#         ny = y
#         cnt = 0
<<<<<<< HEAD
#         while 0<=nx<N and 0<=ny<N and arr[ny][nx]=='o':
#             cnt += 1
#             nx += dx[i]
#             ny += dy[i]
=======

#         while 0<=nx<N and 0<=ny<N and arr[ny][nx] == 'o':
#             cnt += 1
#             nx += dx[i]
#             ny += dy[i]
        
>>>>>>> origin/master
#         if cnt >= 5:
#             ans = 'YES'
#             return

# for t in range(int(input())):
#     N = int(input())
#     arr = [list(map(str, input())) for _ in range(N)]
#     ans = 'NO'

#     for y in range(N):
#         for x in range(N):
#             if arr[y][x] == 'o':
#                 dfs(x,y)
<<<<<<< HEAD

#     print(f'#{t+1} {ans}')



dx = [-1,0,1,1]
dy = [1,1,1,0]

def dfs(x,y):
    global ans
    for i in range(4):
        nx = x
        ny = y
        cnt = 0
        while 0<=nx<N and 0<=ny<N and chess[ny][nx] == 'o':
            cnt += 1
            nx += dx[i]
            ny += dy[i]
        if cnt >= 5:
            ans = 'YES'
            return

for t in range(int(input())):
    N = int(input())
    chess = [list(map(str, input())) for _ in range(N)]
    ans = 'NO'

    for y in range(N):
        for x in range(N):
            if chess[y][x] == 'o':
                dfs(x,y)

    print(f'#{t+1} {ans}')





























# dx = [-1,0,1,1]
# dy = [1,1,1,0]

# def dfs(x,y):
#     global ans
#     for i in range(4):
#         nx = x
#         ny = y
#         cnt = 0

#         while 0<=nx<N and 0<=ny<N and arr[ny][nx] == 'o':
#             cnt += 1
#             nx += dx[i]
#             ny += dy[i]
        
#         if cnt >= 5:
#             ans = 'YES'
#             return

# for t in range(int(input())):
#     N = int(input())
#     arr = [list(map(str, input())) for _ in range(N)]
#     ans = 'NO'

#     for y in range(N):
#         for x in range(N):
#             if arr[y][x] == 'o':
#                 dfs(x,y)
=======
>>>>>>> origin/master

#     print(f'#{t+1} {ans}')