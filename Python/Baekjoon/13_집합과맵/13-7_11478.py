import sys
input = sys.stdin.readline

s = input().rstrip()
s_set = set()

for n in range(len(s)):
    for i in range(1,len(s)+1):
        s_set.add(s[n:n+i])

print(len(s_set))
