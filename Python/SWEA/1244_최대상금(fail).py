from collections import deque
from copy import deepcopy


for t in range(1,int(input())+1):
    num, cnt = map(int,input().split())
    array = list(map(int, str(num)))
    N = len(array)

    if array.count(array[0]) == len(array):
        print("#",t," ",num,sep="")
    
    else:
        queue = deque()
        queue.append((0, array))
        qmax = 0

        while queue:
            dep, arr = queue.popleft()

            if (dep == cnt):
                arrStr = ''
                for i in range(len(arr)):
                    arrStr += str(arr[i])
                qmax = max(qmax, int(arrStr))
            
            else:
                for i in range(N):
                    for j in range(i+1,N):
                        temp = deepcopy(arr)
                        temp[i], temp[j] = temp[j], temp[i]
                        queue.append((dep+1, temp))

        print("#",t," ",qmax,sep="")
