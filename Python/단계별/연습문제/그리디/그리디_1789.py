#똑같지만 더 간단한 풀이
import sys
input = sys.stdin.readline

num, i = 0, 1
S = int(input())

while True:
    i += 1
    num += i

    if num > S: break
print(i-1)


#내풀이
# import sys
# input = sys.stdin.readline

# num, i = 0, 1
# S = int(input())

# while True:
#     num += i

#     if num == S:
#         print(i)
#         break

#     elif num > S:
#         print(i-1)
#         break
    
#     else:
#         i += 1