for T in range(int(input())):
  lst = list(map(str, input().split()))
  N = int(lst[0])
  del lst[0]
  bc, oc = 1,1
  time = 0
  i = 1

  while i<=len(lst):
    if lst[i-1] == 'B':
      if bc == int(lst[i]):
        bc = int(lst[i])
        oc += 1
        time += 1
        i += 2
      elif bc > int(lst[i]):
        if lst[i-3] == 'B':
          oc += bc-int(lst[i])
          time += bc-int(lst[i])+1
          bc = int(lst[i])
          i += 2
        else:
          oc += 1
          time += 1
          bc = int(lst[i])
          i += 2
      else :
        oc += int(lst[i])-bc
        time += int(lst[i])-bc
        bc += int(lst[i])-bc
    
    elif lst[i-1] == 'O':
      if oc == int(lst[i]):
        oc = int(lst[i])
        bc += 1
        time += 1
        i += 2
      elif oc > int(lst[i]):
        if lst[i-3] == 'O':
          bc += oc-int(lst[i])
          time += oc-int(lst[i])+1
          oc = int(lst[i])
          i += 2
        else:
          bc += 1
          time += 1
          oc = int(lst[i])
          i += 2
      else:
        bc += int(lst[i])-oc
        time += int(lst[i])-oc
        oc += int(lst[i])-oc

  print(f'#{T+1} {time}')























# def time(clst):
#   now = 0
#   check = []
#   p = 1
#   for t in clst:
#     if p < t:
#       now += (t-p)+1
#       p = t
#       check.append(now)
#     else:
#       now += (p-t)+1
#       p = t
#       check.append(now)

#   return now, check

# for T in range(int(input())):
#   arr = list(map(str, input().split()))
#   N = arr[0]
#   del arr[0]
#   blst, olst = [], []
#   cb, co = [], []
#   cnt = 0
#   ans = 0

#   for i in range(1,len(arr),2):
#     if arr[i-1] == 'B':
#       blst.append(int(arr[i]))
#     else:
#       olst.append(int(arr[i]))

#   mb, cb = time(blst)
#   mo, co = time(olst)

#   print(cb,co)

#   for b in cb:
#     for o in co:
#       if b==o:
#         cnt += 1

#   ans = max(mb+cnt,mo+cnt)

#   print(f'#{T+1} {ans}')


