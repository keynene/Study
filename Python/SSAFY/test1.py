#전치행렬
arr2 = list(zip(*arr))

#딕셔너리
dic = {}
for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dic.get(want)

#누적합
prefix = [0]
sumValue = 0
for i in arr:
    sumValue += i
    prefix.append(sumValue)

#DP 중요
if j-bag[i-1][0] >= 0: #리미트 걸려잇는거
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i-1][0]] + bag[i-1][1])
else:
    dp[i][j] = dp[i-1][j]



#N-Queen
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
    ans = 0
    v1,v2,v3 = [[0]*(2*N) for _ in range(3)]
    dfs(0)

#검사함수
def check(x,y):
    global ans
    for i in range(dx개수):
        nx = x
        ny = y
        while 0<=nx<N and 0<=ny<N and ..:
            cnt += 1
            nx += dx[i]
            ny += dy[i]
        if cnt >= 5:
            ans = 'YES'
            return