
def dfs(n,res):
    global ans
    if n == N:
        if res == K:
            ans += 1
        return

    dfs(n+1, res)
    dfs(n+1, res+arr[n])


for t in range(int(input())):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    ans = 0

    dfs(0,0)

    print(f'#{t+1} {ans}')






































# def dfs(n, sm):
#     global ans

#     if n == N:
#         if sm == K:
#             ans += 1
#         return
    
#     dfs(n+1, sm+A[n])
#     dfs(n+1, sm)

# for t in range(1,int(input())+1):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
#     ans = 0

#     dfs(0,0)

#     print(f'#{t} {ans}')

