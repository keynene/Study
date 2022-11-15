for tc in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    lst = sorted(list(map(int,input().split())))

    ans = 'Possible'
    cnt = 0
    for t in lst:
        cnt += 1
        if (t//M)*K < cnt:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')


# for t in range(1,int(input())+1):
#     N,M,K = map(int,input().split())
#     c = sorted(list(map(int,input().split())))
#     cnt = 0
#     make = [0]*(c[-1]+1)

#     for i in range(1,len(make)):
#         if i%M == 0:
#             cnt += 1
#             make[i] = K*cnt
#         else: make[i] = make[i-1]
    
#     suc = 0

#     for arrive in c:
#         if make[arrive] > 0:
#             for i in range(arrive,len(make)):
#                 make[i] -= 1
#             suc += 1
#         else:
#             break
    
#     if suc == N: print(f'#{t} Possible')
#     else: print(f'#{t} Impossible')
