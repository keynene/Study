arr = [[0]*141 for _ in range(141)]
pre = [0]
for i in range(1,141):
    pre.append(i)

for i in range(1,141):
    for j in range(1,141):
        arr[i][j] = arr[i][j-1] + pre[j]
    del pre[1]
    pre.append(pre[-1]+1)

print(arr[3][1])








# for t in range(1,int(input())+1):
#     p, q = map(int, input().split())


        
