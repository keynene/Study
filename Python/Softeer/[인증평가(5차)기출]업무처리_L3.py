import sys
from collections import deque
input = sys.stdin.readline

H, K, R = map(int, input().split())
work = [list(map(int, input().split())) for _ in range(2**H)]
cnt = len(work)
day = 1
tmep = []

while(cnt <= 1):
  