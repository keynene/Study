inp = list(map(int,input().split()))
A = inp[0]
B = inp[1]
C = inp[2]
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#A,B,C = map(int,input().split())
#print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep="\n")