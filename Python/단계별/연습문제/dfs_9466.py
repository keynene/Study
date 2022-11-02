import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(v):
    global result
    visited[v] = True
    cycle.append(v)
    num = number[v]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    number = [0] + list(map(int, input().split()))
    visited = [True] + [False]*N
    result = []

    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N-len(result))

























#시간초과
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# t = int(input().rstrip())
# res = []

# def dfs(v, s, pre, cnt):
#     global non_team

#     visited[v] = True
#     pre += str(v)+' '
#     cnt += 1

#     if not visited[want[v]]:
#         dfs(want[v], s, pre, cnt)
    
#     elif visited[want[v]]:
#         if s == want[v]:
#             team.append(list(map(int,pre.split())))
#             non_team += cnt
#         return

# for _ in range(t):
#     n = int(input().rstrip())
#     visited = [False]*(n+1)
#     team = []
#     non_team = 0
#     want = list(map(int, input().split()))
#     want.insert(0,0)

#     for i in range(1,n+1):
#         if not visited[i] or i not in team:
#             pre_team = ''
#             pre_cnt = 0
#             dfs(i, i, pre_team, pre_cnt)
    
#     print(n-non_team)


#17:06  #18:40  #틀렸습니다
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# t = int(input().rstrip())
# res = []

# def dfs(v, s, team):
#     visited[v] = True

#     if not visited[want[v]]:
#         dfs(want[v], s, team)

#     if visited[want[v]]:
#         if want[v] == s:
#             team[v] = 0
#             return
#         elif want[v] == v:
#             team[s] = 1
#             team[v] = 0
#             return
#         else:
#             team[v] = 1
#             return

# for _ in range(t):
#     n = int(input().rstrip())
#     visited = [False]*(n+1)
#     team = [0]*(n+1)
#     want = list(map(int, input().split()))
#     want.insert(0,0)
#     team[0] = 0

#     for i in range(1,n+1):
#         if not visited[i]:
#             dfs(i, i, team)

#     res.append(sum(team))
# print(*res,sep="\n")