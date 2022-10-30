import sys
m,n = map(int, sys.stdin.readline().split())

def sosu(num):
    if num == 1: return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(m, n+1):
    if sosu(i):
        print(i)






###당연한 결과지만, 시간초과###
# import sys
# input = sys.stdin.readline

# m,n = map(int, input().split())
# number = [i for i in range(m,n+1)]
# sosu = []
# for num in number:
#     err = 0
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 err += 1
#         if err == 0:
#             sosu.append(num)
# for i in sosu:
#     print(i)