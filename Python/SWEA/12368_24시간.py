for T in range(1,int(input())+1):
  A,B = map(int, input().split())

  print(f'#{T} {(A+B)%24}')
  
