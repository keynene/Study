# 음식물 피하기
import sys
sys.setrecursionlimit(10 ** 4)


def solution(k):
	global street
	for _ in range(k):
		x, y = map(int, input().split())
		street[x - 1][y - 1] = 1

	results = []
	global result
	for i in range(m):
		for j in range(n):
			if dfs(i, j):
				results.append(result)
				result = 0
	results.sort(reverse=True)
	print(results[0])


def dfs(y,x):
	if 0 <= x < n and 0 <= y < m and street[x][y] == 1:
		global result
		result += 1
		street[x][y] = 0
		dfs(y - 1, x)
		dfs(y, x - 1)
		dfs(y + 1, x)
		dfs(y, x + 1)
		return True
	return False


if __name__ == '__main__':
	n, m, k = map(int, input().split())
	street = [[0 for _ in range(m)] for _ in range(n)]
	result = 0
	solution(k)
