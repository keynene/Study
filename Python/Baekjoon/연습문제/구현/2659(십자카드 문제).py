import sys
input = sys.stdin.readline

def timeNumber(n):
	global cnt
	global minR

	#0들어가면 계산 X
	a,b,c,d = map(int, str(n))
	if 0 in (a,b,c,d):
		minR = 10000
		return

	#시계방향 1바퀴 돌면 끝 + cnt초기화
	if cnt == 4 :
		cnt = 0
		return
	
	#시계방향 돌리면서 min값 찾기
	a,b,c,d = map(str, str(n))
	n = int(str(b+c+d+a))
	minR = min(minR,n)
	cnt += 1
	timeNumber(n)


N = list(map(str, input().split()))
num = "".join(N)
minR = 10000
cnt = 0
timeNumber(num)
comp = minR

#1111부터 입력값의 시계수까지의 시계수 count ++
count = 1 #comp도 시계수니까 1부터시작 (count = 0하고 range(1111, comp+1)해도 됨)
for i in range(1111,comp):
	timeNumber(i)
	if minR == i : count += 1
	minR = 10000

print(count)


