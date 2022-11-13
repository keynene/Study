import sys
import string

s = input()
q = int(input())
# 알파벳별 저장
char_list = {}
for char in string.ascii_lowercase:
    char_list[char] = [0]
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count += 1
        char_list[char].append(count)
        
for _ in range(q):
    char, start, end = sys.stdin.readline().rstrip().split()
    start, end = int(start), int(end)
    print(char_list[char][end + 1] - char_list[char][start])


#문자 a만 하는건줄 알고 틀림
# import sys
# input = sys.stdin.readline

# S = str(input().rstrip())
# q = [list(map(str, input().split())) for _ in range(int(input()))]
# comp = q[0][0]
# p = []
# cnt, idx = 0, 0

# for i in range(len(S)):
#     if S[i] == comp:
#         cnt += 1
#     p.append(cnt)

# for alpha, left, right in q:
#     left,right = int(left), int(right)
#     res = p[right]-p[left]

#     if left > 0:
#         if p[left] == p[left-1]:
#             print(res)
#         else:
#             print(res+1)
#     else:
#         print(res)
