# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# num = []

# def bt():
#     if len(num) == m:
#         print(*num)
#         return
#     for i in range(1,n+1):
#         if len(num)==0 or i>= num[-1]:
#             num.append(i)
#             bt()
#             num.pop()
# bt()


#다른풀이
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = []

def bt(start):
    if len(num) == m:
        print(*num)
        return
    for i in range(start,n+1):
        num.append(i)
        bt(i)
        num.pop()
bt(1)