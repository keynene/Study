import sys
input = sys.stdin.readline

s = str(input().rstrip())
cnt = 0
save = ''
num = []
f = []

for i in range(len(s)):
    save += s[i]
    if s[i]=='+' or s[i]=='-':
        num.append(int(save[0:-1]))
        f.append(s[i])
        save=''
    if i==len(s)-1:
        num.append(int(save))

while len(f)!=0:
    for i in range(len(f)):
        if f[i]=='+':
            num[i] = num[i]+num[i+1]
            del num[i+1]
            del f[i]
            break
        
        elif f[i]=='-' and '+' not in f:  
            num[i+1] *= -1
            num[i] = num[i]+num[i+1]
            del num[i+1]
            del f[i]
            break
print(*num)