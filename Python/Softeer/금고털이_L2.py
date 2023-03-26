import sys
input = sys.stdin.readline

W,N = map(int, input().split())
gold = [list(map(int, input().split())) for _ in range(N)]
gold.sort(key=lambda x:-x[1])
ans = 0

    
for weight, price in gold:
  if W > weight:
    ans += weight * price
    W -= weight
  else:
    ans += W*price
    break
  
print(ans)


