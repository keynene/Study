import sys
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
            
tc = int(sys.stdin.readline())
print(fibo(tc))