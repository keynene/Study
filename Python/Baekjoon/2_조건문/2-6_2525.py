a,b = map(int,(input().split()))
time = int(input())

if b+time >= 60:
    if a+((time+b)//60) > 23:
        a = (a+((time+b)//60))%24
        b = (time+b)%60
    else:
        a = a+((time+b)//60)
        b = (time+b)%60
else:
    b = time+b
    
print(a, b)
