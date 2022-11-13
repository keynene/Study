N = int(input())
firstNum = [N//10,N-((N//10)*10)]; #26 
setNum = firstNum[1];
plusNum = firstNum[0]+firstNum[1]; #8
newNum = [setNum,plusNum-((plusNum//10)*10)] #68
cnt = 1;

while True:
    if firstNum == newNum :
        print(cnt);
        break;
    else:
        saveNum = newNum[1]; #8
        plusNum = newNum[0]+newNum[1]; #14
        newNum = [saveNum,plusNum-((plusNum//10)*10)] #84
        cnt = cnt+1;
