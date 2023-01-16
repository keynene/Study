import sys
input = sys.stdin.readline

halli = [list(map(str, input().split())) for _ in range(int(input().rstrip()))]
st, ba, li, pl = 0,0,0,0

def galli(string, num):
	global st, ba, li, pl

	if string == 'STRAWBERRY':
		st += num
	elif string == 'BANANA':
		ba += num
	elif string == 'LIME':
		li += num
	elif string == 'PLUM':
		pl += num

for a,b in halli:
	galli(a,int(b))

if st==5 or ba==5 or li==5 or pl==5:
	print('YES')
else: print('NO')
