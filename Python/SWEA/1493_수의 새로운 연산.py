for T in range(1,int(input())+1):
  graph = [[0]*10001 for _ in range(10001)]
  p,q = map(int,input().split())
  s1,e1,s2,e2 = 0,0,0,0
  num = 1
  isTrue = False
  temp = 1

  while temp <= 300:
    for y in range(temp,0,-1):
      for x in range(1,y):
        graph[y][x] = num

        if num == p:
          s1 = y
          e1 = x
        
        if num == q:
          s2 = y
          e2 = x

        num += 1

  s3 = s1+s2
  e3 = e1+e2



  print(f'#{T} {graph[s3][e3]}')


  