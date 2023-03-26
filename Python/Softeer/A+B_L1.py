import sys
input = sys.stdin.readline

for T in range(int(input().rstrip())):
    A,B = map(int, input().split())
    print('Case #{}: {}'.format(T+1, A+B))