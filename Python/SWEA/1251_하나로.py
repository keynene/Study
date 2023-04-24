def dfs(v,res):
  global ans
  if len(visited) == N:
    ans = min(ans, res)
  
  for x,y in node:
    if (x,y) in v:
      continue;
    v.append((x,y))
    res = v[-1][0]
    dfs(v)


for T in range(1, int(input())+1):
  N = int(input())
  xArr = map(int, input().split())
  yArr = map(int, input().split())

  node = []
  for x, y in zip(xArr, yArr):
    node.append([x,y])

  visited = {(node[0][0],node[0][1])}
  ans = 9999999999
