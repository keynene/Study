#15:19

#실패한 내 풀이#
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

King,Dol,n = map(str,input().split())
n = int(n)
move = [str(input().rstrip()) for _ in range(n)]

chess = [[0]*8 for _ in range(9)]
switch_alpa = {'':0, 'A':1 ,'B':2 , 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
move_horse = {'R':0, 'RT':1 ,'T':2 , 'LT':3, 'L':4, 'LB':5, 'B':6, 'RB':7}
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
# switch_num = {0:'', 1:'A' , 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}

def kingMove(arr):
    global move_horse

    chess2 = deepcopy(chess)
    queue = deque()
    queue.append((King,1))
    queue.append((Dol,2))
    
    while queue:
        cnt = 0
        horse, type = map(str,queue.popleft())
        type = int(type)
        x, y = map(str, horse)
        y = int(y)
        x = (switch_alpa.get(x))

        if max(map(max, chess2)) <= 1:
            temp = chess2[y][x] = type
            queue.append((horse, type))
        
        else:
            idx = move_horse.get(move[0])
            nx = x+dx[idx]
            ny = y+dy[idx]

            if 0<nx<9 and 0<ny<9 and chess2[ny][nx] == 0:
                chess[y][x] = 0
                chess[ny][nx] = type
                horse = str(nx)+str(ny)
                queue.append((horse,type))

                if type == 2:
                    del move[0]
            elif 0<nx<9 and 0<ny<9 and chess2[ny][nx] != 0:
                if type == 1:
                    horse = str(x)+str(y)
                    queue.append((horse,type))
                else:

    return chess2

kingMove(chess)



###다른사람풀이
# king, stone, N = input().split()
# k = list(map(int, [ord(king[0]) - 64, king[1]]))
# s = list(map(int, [ord(stone[0]) - 64, stone[1]]))
# move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

# for _ in range(int(N)):
#     m = input()
#     nx = k[0] + move[m][0]
#     ny = k[1] + move[m][1]
#     if 0 < nx <= 8 and 0 < ny <= 8:
#         if nx == s[0] and ny == s[1]:
#             sx = s[0] + move[m][0]
#             sy = s[1] + move[m][1]
#             if 0 < sx <= 8 and 0 < sy <= 8:
#                 k = [nx, ny]
#                 s = [sx, sy]
#         else:
#             k = [nx, ny]
# print(f'{chr(k[0] + 64)}{k[1]}')
# print(f'{chr(s[0] + 64)}{s[1]}')




















