import sys
input = sys.stdin.readline

m,n = map(int,input().split())

for i in range(m,n+1):
    err = 0
    for j in range(2, int(i**0.5)+1):
        if i > 1:
            if i%j == 0:
                err += 1
    if err == 0:
        print(i)