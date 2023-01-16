import sys
input = sys.stdin.readline

N = int(input().rstrip())
num = list(map(int, input().split()))
comp = [0]
cnt = 0


for n in num:
	if n-cnt != comp[-1]:
		comp.append(n)
		cnt = 1
	else : cnt += 1

print(sum(comp))

