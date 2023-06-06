for T in range(int(input())):
  n,m = map(int, input().split())
  arr = [list(map(int, str(input().rstrip()))) for _ in range(n)]
  ans = 'yes'

  for y in range(1,n):
    for x in range(m):
      if arr[y][x] == arr[y-1][x]:
        ans = 'no'
        break
    if ans == 'no':
      break

  print(f'{T+1} {ans}')