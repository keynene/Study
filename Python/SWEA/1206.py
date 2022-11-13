import sys
input = sys.stdin.readline

T = 10
for test_case in range(1, T + 1):

    N = int(input())
    building = list(map(int, input().split()))
    cnt = 0

    for i in range(2,len(building)-2):
        if building[i-2] < building[i] and building[i-1] < building[i] and building[i+1] < building[i] and building[i+2] < building[i]:
            maxB = max(building[i-2],building[i-1],building[i+2],building[i+1])
            cnt += (building[i]-maxB)

    print("#",test_case," ",cnt,sep="")