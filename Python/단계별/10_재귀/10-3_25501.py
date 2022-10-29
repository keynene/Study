def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    cnt = 0 
    return recursion(s, 0, len(s)-1, cnt)



import sys
input = sys.stdin.readline

t = int(input().rstrip())
s = [print(*isPalindrome(input().rstrip())) for _ in range(t)]

###다른풀이 (global)###
# import sys


# def recursion(s, l, r):
#     global cnt
#     cnt += 1;

#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

# for _ in range(int(input())):
#     cnt = 0
#     print(isPalindrome(sys.stdin.readline().strip()),cnt)