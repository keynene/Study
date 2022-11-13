a,b = input(),input()
a,b = int(a), int(b)
b_100 = b//100
b_10 = (b-(b_100*100))//10
b_1 = b%10
print(a*b_1, a*b_10, a*b_100, a*b, sep='\n')

