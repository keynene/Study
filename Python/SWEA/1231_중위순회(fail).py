for T in range(1,11):
  N = int(input())
  node = [list(map(str, input().split())) for _ in range(N)]
  ans = ''
  visited = [False]*N

  #트리순회