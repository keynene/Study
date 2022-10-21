import sys
input = sys.stdin.readline

n = int(input().rstrip())
time = sorted(list(map(int,input().split())))
waiting = []

plus = 0
for order in time:
    plus += order
    waiting.append(plus)

print(sum(waiting))