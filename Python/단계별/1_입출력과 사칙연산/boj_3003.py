chess = [1,1,2,2,2,8]
a = list(map(int,input().split()))
#map : 배열의 요소의 타입을 한꺼번에 바꿔줌
for i in range(6):
    print(chess[i]-a[i], end=' ')
#print 속성 end : 출력시 \n 기준으로 출력되는데 이를 다른 문자로 변경