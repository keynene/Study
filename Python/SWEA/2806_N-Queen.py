def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

for t in range(int(input())):
    N = int(input())
    v1,v2,v3 = [[0]*(2*N) for _ in range(3)]
    ans = 0

    dfs(0)

    print(f'#{t+1} {ans}')





























# from copy import deepcopy

# dx = [1,1,0,-1,-1,-1,0,1]
# dy = [0,-1,-1,-1,0,1,1,1]

# def visit(x,y,arr):
#     varr = deepcopy(arr)
#     for i in range(8):
#         nx = x
#         ny = y
#         while 0<=nx<N and 0<=ny<N:
#             varr[ny][nx] = True
#             nx += dx[i]
#             ny += dy[i]
#     return varr

# def dfs(n,chess):
#     global ans,cnt

#     if n == N:
#         ans += 1
#         return

#     for y in range(n,N):
#         cnt = 0
#         for x in range(N):
#             if not chess[y][x]:
#                 cnt += 1
#                 temp = visit(x,y,chess)
#                 dfs(n+1,temp)
#         if cnt < 1:
#             break

# for t in range(int(input())):
#     N = int(input())
#     chess = [[False]*N for _ in range(N)]
#     ans = 0
#     cnt = 0

#     dfs(0,chess)

#     print(f'#{t+1} {ans}')




































##현진이함수
# import copy

# def fillRow(copyRow , x, y) :
    
#     global n 
#     frow = copy.deepcopy(copyRow)
#     for i in range (n) :  ## 가로새로 채우기
#         frow[y][i] = 1
#         frow[i][x] = 1
  
#     nx = x
#     ny = y
#     while True :  ## 대각선 채우기
#         nx = nx+ 1
#         ny = ny+ 1 
#         if nx >= n or ny >= n :
#             break;
#         frow[ny][nx] = 1
        
#     nx = x
#     ny = y
#     while True : ## 대각선 채우기
#         nx = nx- 1
#         ny = ny+ 1 
#         if nx < 0  or ny >= n :
#             break;
#         frow[ny][nx] = 1
        
#     nx = x
#     ny = y    
    
#     while True :  ## 대각선 채우기
#         nx = nx+ 1
#         ny = ny- 1 
#         if nx >= n or ny < 0 :
#             break;
#         frow[ny][nx] = 1    
        
#     nx = x
#     ny = y       
            
#     while True :  ## 대각선 채우기
#         nx = nx- 1
#         ny = ny- 1 
#         if nx < 0 or ny < 0 :
#             break;
#         frow[ny][nx] = 1        
    
#     return frow

# def dfs(count , copyRow) :
#     global ans
#     global n 
#     if count == n :
#         ans =ans + 1
#         return
    
#     for i in range(n) : 
#         if copyRow[i][count] != 1 :
#             dfs(count+1 ,fillRow(copyRow, count , i))            

# def solution(n1):
#     global n 
#     answer = 0
#     n = n1
#     row = [[0] * n for i in range(n)]
#     dfs( 0 , row)
#     return answer

# n = 0
# ans = 0

# solution(int(input()))

# print(ans)




##문어아저씨
# def dfs(n):
#     global ans
#     if n == N:
#         ans += 1
#         return
    
#     for j in range(N):
#         if v1[j] == v2[n+j] == v3[n-j] == 0:
#             v1[j] = v2[n+j] = v3[n-j] = 1
#             dfs(n+1)
#             v1[j] = v2[n+j] = v3[n-j] = 0

# for t in range(int(input())):
#     N = int(input())
#     ans = 0

    # v1,v2,v3 = [[0]*(2*N) for _ in range(3)]
    # dfs(0)
    # print(f'#{t+1} {ans}')
