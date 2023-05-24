from collections import deque
import sys
input = sys.stdin.readline

# def dfs(n,v):
#   global ans
#   if n == mx:
#     print(v)
#     for i in v:
#       if i<=a and i<=b:
#         ans = min(ans, i)
#     return

#   if graph[n] != []:
#     for e in graph[n]:
#       if e not in v:
#         dfs(e, v+[e])
#   else:
#     for i in range(n,0,-1):
#       if n in graph[i] and i not in v:
#         dfs(i, v+[i])
  

def dfs(s,v):
  global ans
  if a in v and b in v:
    ans = min(v)
    return
  
  for i in range(1,N+1):
    if i not in v and 


N = int(input())
node = [list(map(int, input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N+1)]

for u,v in node:
  if u < v:
    graph[u].append(v)
  else:
    graph[v].append(u)

for M in range(int(input())):
  a,b = map(int, input().split())
  ans = N+1
  # nx = min(a,b)
  # mx = max(a,b)

  # dfs(nx,[nx])

  dfs(1,[])
  
  print(ans)
