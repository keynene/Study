import sys
input = sys.stdin.readline

s = input().rstrip()
s_set = set()

for n in range(len(s)):
    for i in range(1,len(s)+1):
        j = n+i
        s_set.add(s[n:j])

print(len(s_set))
