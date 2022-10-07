def d(n):
    m = 0;
    if n < 10 :
        m = n+n;
    elif n < 100 :
        m = n + n//10 + (n-(n//10*10));
    elif n < 1000 :
        m = n + n//100 + ((n-n//100*100)//10) + (n-(n//10*10));
    elif n < 10000 :
        m = n + (n//1000) + ((n-n//1000*1000)//100) + ((n-(n//100*100))//10) + (n-(n//10*10));
    return m

num = [0]*10000
selfNum = [0]*10000

for i in range(10000):
    num[i] = d(i);
    selfNum[i] = i;

for j in num :
    if selfNum[i] == j :
        continue;
    else :
        print(selfNum[i])

        모르겟다
