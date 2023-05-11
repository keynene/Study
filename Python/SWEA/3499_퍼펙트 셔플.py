for T in range(1,int(input())+1):
  N = int(input())
  card = list(map(str, input().split()))
  sCard = card[:N//2+N%2]
  ans = []
  odd = False

  if N%2 == 0:
    eCard = card[N//2:]
  else:
    odd = True
    eCard = card[N//2+1:]

  for i in range(len(eCard)):
    ans.append(sCard[i])
    ans.append(eCard[i])

  if odd:
    ans.append(sCard[-1])

  print('#{} '.format(T),end="")
  print(*ans)