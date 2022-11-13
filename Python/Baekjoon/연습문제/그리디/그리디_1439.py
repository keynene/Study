import sys
input = sys.stdin.readline

S = list(map(str, str(input().rstrip())))
cnt = 0

for i in range(1,len(S)):
    if S[i-1] != S[i] and S[i] != S[0]:
        cnt += 1
print(cnt)

#다른사람풀이
# n=input()
# count = 0
# for i in range(len(n)-1):
#     if n[i] != n[i+1]:
#         count += 1

# print((count + 1) //2)