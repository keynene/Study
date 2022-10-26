import sys
input = sys.stdin.readline

pobi = [[97,98], [131,132], [99,102]]
crong = [[197,198], [211,212], [211,212]]

def mult(num):
    n = len(str(num))
    res = 0
    if n == 1 :
        res = num
    elif n == 2 :
        a,b = map(int,str(num))
        res = a*b
    elif n == 3 :
        a,b,c = map(int, str(num))
        res = a*b*c
    return res

result = []

for i in range(len(pobi)):

    if pobi[i][0] > 0 and crong[i][0] > 0 and (pobi[i][1]-pobi[i][0]) == 1 and (crong[i][1]-crong[i][0]) == 1:
        pobiRes = []
        crongRes = []

        for numP, numC in zip(pobi[i], crong[i]):
            pobiRes.append(sum(map(int,str(numP))))
            crongRes.append(sum(map(int,str(numC))))
            pobiRes.append(mult(numP))
            crongRes.append(mult(numC))
            
        if max(pobiRes) > max(crongRes):
            result.append(1)
        elif max(pobiRes) < max(crongRes):
            result.append(2)
        elif max(pobiRes) == max(crongRes):
            result.append(0)
    else:
        result.append(-1)


print('| pobi       | crong      | result |','| ---------- | ---------- | ------ |',sep="\n")
for i,j,k in zip(pobi,crong,result):
    pob = ' '*(10-len(str(i)))
    cro = ' '*(10-len(str(j)))
    sp = ' '*(6-len(str(k)))
    print('| ',i,pob,' |',' ', j, cro, ' |', ' ', k, sp, ' |',sep="")