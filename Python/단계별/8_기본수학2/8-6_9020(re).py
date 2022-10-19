import sys
input = sys.stdin.readline

t = int(input().rstrip())

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(t):
    n = int(input().rstrip())
    a,b = n//2, n//2
    while a > 0:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1





### 시간초과 (맞왜틀) ### 
import sys
input = sys.stdin.readline

t = int(input().rstrip())

def prime(n):
    res = []
    res_prime = ''
    for num in range(n):
        err = 0
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                err += 1
        if err == 0:
            res.append(num)
    cnt = max(res)-min(res)
    for a in res:
        for b in res:
            if a+b == n:
                if abs(a-b) < cnt:
                    cnt = abs(a-b)
                    res_prime = str(a)+' '+str(b)
                else:
                    pass
    return res_prime

for _ in range(t):
    n = int(input().rstrip())
    print(prime(n))