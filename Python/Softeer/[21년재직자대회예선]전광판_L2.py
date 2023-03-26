import sys
input = sys.stdin.readline

num = {'0':[0,0,0,0,0,0,0], 
       '1':[0,0,1,0,0,1,0], 
       '2':[1,0,1,1,1,0,1], 
       '3':[1,0,1,1,0,1,1], 
       '4':[0,1,1,1,0,1,0], 
       '5':[1,1,0,1,0,1,1], 
       '6':[1,1,0,1,1,1,1], 
       '7':[1,1,1,0,0,1,0], 
       '8':[1,1,1,1,1,1,1], 
       '9':[1,1,1,1,0,1,1],
       'a':[1,1,1,0,1,1,1]}

def transfort(n):
  if len(n) == 1:
    return '0000'+n
  elif len(n) == 2:
    return '000'+n
  elif len(n) == 3:
    return '00'+n
  elif len(n) == 4:
    return '0'+n
  else: return n
  
def find_A(n):
  temp = n[0]
  
  for i in range(1,5):
    if temp != 0 and n[i]==0:
      n[i] = 'a'
    temp = n[i]
      
  return n

def comp(a,b):
  global cnt
  a_num = num.get(str(a))
  b_num = num.get(str(b))
  
  for i in range(7):
    if a_num[i] != b_num[i]:
      cnt += 1
    
for _ in range(int(input().rstrip())):
  start, end = map(str, input().split())
  start = find_A(list(map(int,str(transfort(start)))))
  end = find_A(list(map(int,str(transfort(end)))))
  cnt = 0
  
  for i in range(5):
    if start[i] != end[i]:
      comp(start[i],end[i])
      
  print(cnt)