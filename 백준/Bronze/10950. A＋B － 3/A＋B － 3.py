T = int(input())
A,B,C = [0]*T, [0]*T, [0]*T
for i in range(T):
    A[i],B[i] = input().split()
    C[i] = int(A[i])+int(B[i])
for i in range(T):
    print(C[i])