for t in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(zip(*arr))
    
    ans = 0
    for lst in arr_t:
        prev = 0
        for n in lst:
            if n:
                if n == 2 and prev == 1:
                    ans += 1
                prev = n
    
    print(f'#{t} {ans}')




# from copy import deepcopy

# for t in range(1,11):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     arr2 = deepcopy(arr)
#     cnt = 1

#     while cnt > 0:
#         cnt = 0
#         for i in range(N):
#             for j in range(N):
#                 if arr[i][j] == 1:
#                     if i > 0 and arr[i-1][j] != 2 and arr2[i-1][j] != 2:
#                         cnt += 1
#                         arr2[i][j] = 0
#                         arr2[i-1][j] = 1
#                     elif i == 0:
#                         cnt += 1
#                         arr2[i][j] = 0

#                 elif arr[i][j] == 2:
#                     if i < N-1 and arr[i+1][j] != 1 and arr2[i+1][j] != 1:
#                         cnt += 1
#                         arr2[i][j] = 0
#                         arr2[i+1][j] = 2
#                     elif i == N-1:
#                         cnt += 1
#                         arr2[i][j] = 0
#         arr = deepcopy(arr2)
#     ans = 0
#     for i in range(N-1):
#         for j in range(N):
#             if arr[i][j] == 2 and arr[i+1][j] == 1:
#                 ans += 1
    
#     print(f'#{t} {ans}')