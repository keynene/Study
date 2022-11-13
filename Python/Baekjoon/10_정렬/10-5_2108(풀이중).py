import sys


tc = int(input())

n = [int(sys.stdin.readline()) for _ in range(tc)]
sort_n = sorted(n)

#1
avg_1 = sum(n)/tc
print("1.산술평균:",round(avg_1))

#2
avg_2 = sort_n[tc//2]
print("2.중앙값:",avg_2)

#3





#4
print("4.범위:",max(n)-min(n))