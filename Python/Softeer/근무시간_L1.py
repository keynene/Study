import sys
input = sys.stdin.readline

time = [list(map(str, input().split()))for _ in range(5)]
hour, min = 0,0


for start, end in time:
  start_h, start_m = map(int,start.split(":"))
  end_h, end_m = map(int,end.split(":"))
  
  hour += end_h-start_h
  if end_m >= start_m: min += end_m-start_m
  else: 
    min += 60-start_m + end_m
    hour -= 1

print(hour*60+min)