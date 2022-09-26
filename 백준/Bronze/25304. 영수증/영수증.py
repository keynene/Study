import sys
X = int(input())
plus = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    plus = plus+a*b
print('Yes' if X==plus else 'No');