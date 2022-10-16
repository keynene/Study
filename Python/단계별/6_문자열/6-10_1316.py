import sys
input = sys.stdin.readline

n = int(input().strip())
word = [input().strip() for _ in range(n)]
group = n

for test in word:
    check = {}
    check_len = 0
    check.clear()
    for i in range(len(test)):
        if test[i:i+1] in check:
            if test[i:i+1] == test[i-1:i]:
                check[test[i:i+1]] += 1
                check_len += 1
            else:
                break
        else:
            check[test[i:i+1]] = 1
            check_len += 1
    if check_len != len(test):
        group -= 1
        
print(group)



#다른풀이

import sys
input = sys.stdin.readline

n = input().strip()
cnt = n

for i in range(n):
    word = input().strip()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)