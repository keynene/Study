def solve(a):
    num = 0;
    for i in range(len(a)):
        if isinstance(a[i],int) == True :
            num = num+a[i]
    return num