import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
ans = ''

if num[0]+7 == num[7]:
	for i in range(1,8):
		if num[i]-num[i-1] != 1:
			ans = 'mixed'
			break
	if ans == '' : print('ascending')
	else: print('mixed')

elif num[0]-7 == num[7]:
	for i in range(1,8):
		if num[i-1]-num[i] != 1:
			ans = 'mixed'
			break
	if ans == '' : print('descending')
	else: print('mixed')
	
else:
	print('mixed')