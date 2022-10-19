import sys
input = sys.stdin.readline

def gj(n):
    err = 0
    for j in range(2,int((n**0.5))+1):
        if n%j == 0:
            return False
    if err == 0:
        return True

cnt = 0

while True:
    n = int(input().rstrip())
    cnt = 0
    if n != 0:
        for i in range(n+1,(2*n)+1):
            if gj(i):
                cnt += 1
        print(cnt)
    else:
        break