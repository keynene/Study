import sys
input = sys.stdin.readline

N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
comp = list(map(int, input().split()))

dic = {}
for i in card:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

def bs(start, end, arr, target):
    if start > end:
        return 0
    mid = (start+end)//2

    if arr[mid] > target:
        return bs(start, mid-1, arr, target)

    elif arr[mid] < target:
        return bs(mid+1, end, arr, target)

    else:
        return dic.get(target)

for i in comp:
    print(bs(0, len(card)-1, card, i), end=" ")