import sys
while True:
    try:
        a,b = map(int,sys.stdin.readline().split())
    except:
        break;
    print(a+b)

# 어떤 코드가 동작하는 과정에서, 오류가 발생할 수도 있고 발생하지 않을 수도 있습니다.
# 이 때 오류를 컨트롤하기 위해 사용하는 것이 try-except-else-finally 구문입니다.
# 들어오는 입력이 없을 경우 5번 라인의 a,b=map(int,sys.stdin.readline().split()) 에서 오류가 발생하게 되고,
# except 구문으로 넘어가 while문에서 break가 일어나게 됩니다.
# 반대로 입력이 계속 진행되고 있는 도중에는 except로 넘어가지 않고, try-except가 끝난 다음인 8번 라인의 print(a+b)를 실행하게 되어 정상 동작하게 되는 것입니다.