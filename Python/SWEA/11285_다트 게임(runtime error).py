for t in range(int(input())):
    N = int(input())
    ans = 0

    for i in range(N):
        x,y = map(int,input().split())
        r = ((x**2 + y**2)**0.5)/20
        if r == 0:
            ans += 10
        elif r <= 11:
            ans += (11-r)

    print(f'#{t+1} {ans}')

