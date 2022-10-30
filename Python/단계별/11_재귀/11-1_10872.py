
def fac(n):
    res = 1
    if n > 0:
        res = n * fac(n-1)
    return res

n = int(input())
print(fac(n))



# def fac(n):
#     if n == 0:
#         return 1
#     return n * fac(n-1)

# n = int(input())
# print(fac(n))




#내풀이
# n = int(input())

# def fac(n,res):
#     if n == 1:
#         res *= n
#         return res

#     res *= n
#     return fac(n-1,res)

# print(fac(n,1))