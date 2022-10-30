import sys

tc = int(sys.stdin.readline().strip())
cnt = 0;
num = 0;

while cnt < tc :
    str_num = str(num)
    if str_num.count('666'):
        cnt += 1;
    num +=1;
      
print(num-1)


#다른풀이
tc = int(sys.stdin.readline().strip())
cnt = 0;
num = 666;

while True :
    if '666' in str(num):
        cnt += 1
    if cnt == num :
        print(num)
        break
    num += 1