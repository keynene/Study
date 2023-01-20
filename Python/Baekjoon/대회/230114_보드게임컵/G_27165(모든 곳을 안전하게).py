import sys
from copy import deepcopy
input = sys.stdin.readline

def backgammon(i,a):
	global ans,s,e
	arr = deepcopy(a)

	if 0<=i<x:
		arr[i] -= 1
		arr[i+x] += 1
		if arr.count(1) == 0:
			ans = 'YES'
			s,e = i, i+x
			return True

	elif x <= i <= (i-x):
		arr[i] -= 1
		arr[i+x] += 1
		if arr.count(1) == 0:
			ans = 'YES'
			s,e = i, i+x
			return True
		arr[i] += 1
		arr[i+x] -= 1

		#####

		arr[i] += 1
		arr[i-x] -= 1
		if arr.count(1) == 0:
			ans = 'YES'
			s,e = i, i+x
			return True

	elif i-x < i <= n:
		arr[i] += 1
		arr[i-x] -= 1
		if arr.count(1) == 0:
			ans = 'YES'
			s,e = i-x, i
			return True

n = int(input().rstrip())
a = list(map(int, input().split()))
x = int(input().rstrip())
s,e,ans = -1,-1,'NO'
cnt = a.count(1)

if cnt == 0:
	for i in range(n):
		if a[i] > 0:
			if backgammon(i,a):
				break

elif cnt == 2:
	for i in range(len(a)):
		if a[i] == 1: 
			if s == -1: s = i
			else: e = i
	if e-s == x:
		ans = 'YES'

elif cnt == 1:
	for i in range(len(a)):
		if a[i] == 1: 
			if i-x >= 0:
				if a[i-x] > 0:
					ans = 'YES'
					s,e = i,i-x
			if i+x <= n:
				if a[i+x] > 0:
					ans = 'YES'
					s,e = i,i+x
			break

print(ans)
if ans == 'YES':
	print(s,e)