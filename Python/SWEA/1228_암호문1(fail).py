for t in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
    K = int(input())
    lst = list(input().split())
    while lst:
        if lst[0] == 'I':
            idx = int(lst[1])+1
            cnt = int(lst[2])+1
            del lst[0], lst[1], lst[2]
            for i in range(idx,cnt+1):
                arr.insert(i, lst[0])
                del lst[0]
    print(arr)
        

