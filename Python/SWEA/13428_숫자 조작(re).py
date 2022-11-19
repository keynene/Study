def dfs(n):
    global minR, maxR
    if n > 0:
        maxR = max(maxR, int("".join(map(str, arr))))
        minR = min(minR, int("".join(map(str, arr))))
        return

    for i in range(L-1):
        for j in range(i+1,L):
            arr[i],arr[j] = arr[j],arr[i]
            chk = int("".join(map(str, arr)))
            if (n, chk) not in v and arr[0] != 0:
                v.append((n,chk))
                dfs(n+1)
            arr[i],arr[j] = arr[j],arr[i]

for t in range(int(input())):
    minR = maxR = int(input())
    arr = list(map(int, str(minR)))
    L = len(arr)
    v = []

    dfs(0)

    print(f'#{t+1} {minR} {maxR}')