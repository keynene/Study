# def d(n):
#     m = 0;
#     if n < 10 :
#         m = n+n;
#     elif n < 100 :
#         m = n + n//10 + (n-(n//10*10));
#     elif n < 1000 :
#         m = n + n//100 + ((n-n//100*100)//10) + (n-(n//10*10));
#     elif n < 10000 :
#         m = n + (n//1000) + ((n-n//1000*1000)//100) + ((n-(n//100*100))//10) + (n-(n//10*10));
#     return m

# print(d(13))
# print(d(123))
# print(d(1234))

# # noSelf = [0]*10000 #self넘버가 아닌 수 저장
# # selfNum = [0]*10000 # 1~10000까지 수 저장

# # for i in range(10000):
# #     noSelf[i] = d(i); 
# #     selfNum[i] = i;

# # for j in num :
# #     if selfNum[i] == j :
# #         continue;
# #     else :
# #         print(selfNum[i])

#생성자 만드는 함수 d(n)
def d(n):
    n = n + sum(map(int,str(n)))
    return n

#셀프넘버가 아닌 수들(생성자가 있는 수들)이 들어갈 집합
#※집합은 자동으로 중복 제거하기 때문에 나중에 따로 중복제거해줄 필요가 없음!
nonSelfNum = set();

#nonSelfNum 집합에 들어갈 수들 넣기 (1~10000)
for i in range(1,10001):
    nonSelfNum.add(d(i)) #1 부터 10000까지 d함수에 들어간 생성자들 넣음 (set이므로 중복제거됨)

#셀프넘버 출력하기
for j in range(1,10001):
    if j not in nonSelfNum:  #1부터 10000까지 숫자 중 nonSelfNum에 저장된 생성자가 있는 수들을 제외하고 출력함
        print(j)

