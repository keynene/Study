def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(map(str,lst))))
        return
    
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str,lst)))
            if (n, chk) not in V:
                dfs(n+1)
                V.append((n,chk))

            lst[i], lst[j] = lst[j], lst[i]

for tc in range(int(input())):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))
    L = len(lst)
    ans = 0
    V = []
    dfs(0)
    print(f'#{tc+1} {ans}')


# from collections import deque
# from copy import deepcopy


# for t in range(1,int(input())+1):
#     num, cnt = map(int,input().split())
#     array = list(map(int, str(num)))
#     N = len(array)

#     if array.count(array[0]) == len(array):
#         print("#",t," ",num,sep="")
    
#     else:
#         queue = deque()
#         queue.append((0, array))
#         qmax = 0

#         while queue:
#             dep, arr = queue.popleft()

#             if (dep == cnt):
#                 arrStr = ''
#                 for i in range(len(arr)):
#                     arrStr += str(arr[i])
#                 qmax = max(qmax, int(arrStr))
            
#             else:
#                 for i in range(N):
#                     for j in range(i+1,N):
#                         temp = deepcopy(arr)
#                         temp[i], temp[j] = temp[j], temp[i]
#                         queue.append((dep+1, temp))

#         print("#",t," ",qmax,sep="")
