import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int,input().split())
    imfort = list(map(int, input().split()))
    cnt = 0

    queue = deque()

    for i in range(N):
        queue.append((i, imfort[i]))

    while queue:
        idx, imfo = queue.popleft()

        if imfo == max(imfort):
            cnt += 1
            if idx == M:
                print(cnt)
                break
            else:
                imfort[idx] = 0
        else:
            queue.append((idx, imfo))


# #12:43  #1:13 첫 성공코드
# import sys
# from collections import deque
# from copy import deepcopy
# input = sys.stdin.readline

# def order(m,doc):
#     queue = deque()
#     for i in range(len(doc)):
#         queue.append((i, doc[i]))
#     comp = max(doc)
#     comp_doc = comp.sort(key=lambda x:-x)
#     cnt = 1
    
#     while queue:
#         idx,docu = queue.popleft()
#         if comp[0] == docu:
#             if idx == m:
#                 print(cnt)
#                 return
#             else:
#                 del comp[0]
#                 cnt += 1
#         else:
#             queue.append((idx,docu))

# for _ in range(int(input())):
#     N,M = map(int,input().split())
#     document = list(map(int, input().split()))
#     order(M,document)