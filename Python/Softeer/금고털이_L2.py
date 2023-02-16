import sys
input = sys.stdin.readline

W,N = map(int, input().split())
gold = [[10000,0]]+sorted([list(map(int, input().split())) for _ in range(N)])
dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1,N+1):
	for j in range(1,W+1):
		if j <= gold[i][0]:
			if j > gold[i-1][0]:
				dp[i][j] = max(dp[i-1][j]+(gold[i][0]-j)*gold[i][1], gold[i][1]*j)
			else:
				dp[i][j] = max(dp[i-1][j], gold[i][1]*j)
		else:
			if j < gold[i][0]+gold[i-1][0]:
				dp[i][j] = max(gold[i-1][1]*gold[i-1][0]+(j-gold[i-1][0])*gold[i][1], gold[i][1]*gold[i][0]+(j-gold[i][0])*gold[i-1][1])

print(dp[N][W])