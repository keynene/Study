import sys
C = int(input())
N = 0;

for i in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    cnt = 0;
    for j in score:
        if j == 0 :
            continue;
        else:
            avg = (sum(score)-score[0])/score[0]
            if score[j] > avg :
                cnt += 1
            else:
                continue;
    print(cnt/score[0])
