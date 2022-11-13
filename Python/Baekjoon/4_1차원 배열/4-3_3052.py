import sys
A = [0]*10
C = [0]*10
for i in range(10):
    A = int(input())
    C[i] = A % 42
C = set(C) #중복요소 제거
print(len(C))  #중복요소 제거한 배열크기


# arr = []
# for i in range(10):
#     n = int(input())
#     arr.append(n % 42)
# arr = set(arr)
# print(len(arr))