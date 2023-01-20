import sys
from copy import deepcopy
input = sys.stdin.readline

def backgammon(x,a):
	global s,e,ans
	arr = deepcopy(a)

	for i in range(2):
		nx = x+dx[i]

		if 0 <= nx <= n :
			if arr[nx] == 1 or arr[nx] > 2:
				arr[nx] -= 1
				arr[x] += 1
				if arr.count(1) == 0:
					ans = 'YES'
					s = x
					e = nx
					return True
	return False

n = int(input().rstrip())
a = list(map(int, input().split()))
m = int(input().rstrip())
s,e,ans = 0,0,'NO'
dx = [-m,m]

for i in range(len(a)):
	if a[i] == 1:
		if backgammon(i,a):
			break

print(ans)
if ans == 'YES':
	print(s,e)






















# import sys
# from copy import deepcopy
# input = sys.stdin.readline

# def backgammon(x,a):
# 	global s,e,ans
# 	nx = x+m
# 	arr = deepcopy(a)

# 	if nx <= n:
# 		arr[x] -= 1
# 		arr[nx] += 1
# 		if arr.count(1) == 0:
# 			ans = 'YES'
# 			s = x
# 			e = nx
# 			return True
# 	return False

# n = int(input().rstrip())
# a = list(map(int, input().split()))
# m = int(input().rstrip())
# s,e,ans = 0,0,'NO'

# for i in range(len(a)):
# 	if a[i] != 2 and a[i] != 0:
# 		if backgammon(i,a):
# 			break

# print(ans)
# if ans == 'YES':
# 	print(s,e)


















# import sys
# from copy import deepcopy
# input = sys.stdin.readline

# def backgammon(x,a):
# 	global s,e,ans
# 	arr = deepcopy(a)

# 	for i in range(2):
# 		nx = x+dx[i]

# 		if nx >= 0 and nx <= len(a)-1:
# 			arr[x] -= 1
# 			arr[nx] += 1
# 			if arr.count(1) == 0:
# 				ans = 'YES'
# 				s = x
# 				e = nx
# 				return True
# 	return False

# n = int(input().rstrip())
# a = list(map(int, input().split()))
# m = int(input().rstrip())
# s,e,ans = 0,0,'NO'
# dx = [-m, m]

# for i in range(len(a)):
# 	if a[i] == 1 or a[i] > 2:

# 		if i-m >= 0 and i+m<=n :
# 			for j in range(i-m+1, i+m-1):
# 				if a.count(1) > 1:
# 					break

# 		if backgammon(i,a):
# 			break

# print(ans)
# if ans == 'YES':
# 	print(s,e)