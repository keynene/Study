import sys
input = sys.stdin.readline

def gj(n):
    for j in range(2,int((n**0.5))+1):
        if n%j == 0:
            return False
    return True

cnt = 0

while True:
    n = int(input().rstrip())
    cnt = 0
    if n == 0:
        break
    else:
        for i in range(n+1,(2*n)+1):
            if gj(i):
                cnt += 1
        print(cnt)



#다른풀이
num = []

for i in range(2, 246913):
    cnt = 0

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break

    if cnt == 0:
        num.append(i)

while True:
    n = int(input())
    res = 0

    if n == 0:
        break

    for i in num:
        if n < i <= 2*n:
            res += 1

    print(res)