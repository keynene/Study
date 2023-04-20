
def comp(i,x):
  if x == '(':
    for j in range(i+1,L):
      if arr[j] == ')':
        arr[i] = '0'
        arr[j] = '0'
        return True
      
  if x == '[':
    for j in range(i+1,L):
      if arr[j] == ']':
        arr[i] = '0'
        arr[j] = '0'
        return True
      
  if x == '{':
    for j in range(i+1,L):
      if arr[j] == '}':
        arr[i] = '0'
        arr[j] = '0'
        return True
      
  if x == '<':
    for j in range(i+1,L):
      if arr[j] == '>':
        arr[i] = '0'
        arr[j] = '0'
        return True
  return False


for T in range(1,11):
  L = int(input())
  arr = list(map(str, input().rstrip()))
  ans = 1

  for i in range(L-1):
    if ans == 0:
      break;
    if arr[i] != '0':
      if not comp(i,arr[i]):
        ans = 0

  print('#{} {}'.format(T,ans))


