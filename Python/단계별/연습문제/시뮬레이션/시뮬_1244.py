import sys
input = sys.stdin.readline

n = int(input())
switch = [0]+list(map(int, input().split()))
student = [list(map(int, input().split())) for _ in range(int(input()))]

for type, num in student:
    if type == 1:
        for i in range(num,n+1,num):
            if switch[i] == 1: switch[i] = 0
            elif switch[i] == 0: switch[i] = 1

    elif type == 2:
        i = 1
        if switch[num] == 0: switch[num] = 1
        elif switch[num] == 1: switch[num] = 0

        while num-i > 0 and num+i < n+1:
            if switch[num-i] == switch[num +i]:
                if switch[num-i] == 1:
                    switch[num-i] = 0
                    switch[num+i] = 0
                    i += 1
                elif switch[num-i] == 0:
                    switch[num-i] = 1
                    switch[num+i] = 1
                    i += 1
            else:
                break

for i in range(1,n+1):
    print(switch[i], end=" ")
    if i%20 == 0:
        print()



# #1:17

# import sys
# from copy import deepcopy
# n = int(input())
# switch = list(map(int,input().split()))
# student = [list(map(int,input().split())) for _ in range(int(input()))]

# def onoff(arr,type,n):
#     switch2 = deepcopy(arr)

#     if type == 1:
#         i = 1
#         while i*(n+1) <= len(arr):
#             if i*(n+1) <= len(arr):
#                 if switch2[i*(n+1)-1] == 0:
#                     switch2[i*(n+1)-1] = 1
#                     i += 1
#                 elif switch2[i*(n+1)-1] == 1:
#                     switch2[i*(n+1)-1] = 0
#                     i += 1
#             else:
#                 break

#     elif type == 2:
#         if switch2[n] == 0:
#             switch2[n] = 1
#         elif switch2[n] == 1:
#             switch2[n] = 0

#         i = 1
#         while n+i<len(arr):
#             if 0<=n-i and n+i<len(arr):
#                 if arr[n-i] == arr[n+i]:
#                     if switch2[n-i] == 0:
#                         switch2[n-i] = 1
#                         switch2[n+i] = 1
#                         i += 1
#                     elif switch2[n-i] == 1:
#                         switch2[n-i] = 0
#                         switch2[n+i] = 0
#                         i += 1
#                 else: break
#             else: break
#     return switch2

# for type, num in student:
#     switch = onoff(switch,type,num-1)

# for i in range(0,n,20):
#     print(*switch[i:i+20])