import sys
input = sys.stdin.readline

crazy = [list(map(str, input().split())) for _ in range(int(input().rstrip()))]
time = 1
ans = ''
mcnt = 0

for a,b in crazy:
	ans = 'NO'
	if int(b) == time :
		if a == 'HOURGLASS':
			ans = 'NO'
		else:
			ans = 'YES'

	elif a == 'HOURGLASS':
		if mcnt == 0:
			mcnt = 1
		else:
			mcnt = 0
	print(time, ans)
	
	if mcnt == 0:
		time += 1
		if time > 12:
			time = 1
	else: 
		time -= 1
		if time < 1:
			time = 12

