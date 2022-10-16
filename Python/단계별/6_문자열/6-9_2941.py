import sys
input = sys.stdin.readline

cro = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
s = input().strip()

for i in cro:
    s = s.replace(i,"*")
print(len(s))

# .replace("찾을값", "바꿀값", [바꿀횟수])