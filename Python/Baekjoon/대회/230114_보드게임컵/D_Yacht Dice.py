import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
dice = list(map(int, input().split()))
ans = [0]*12

for i in range(0,12):
	if arr[i] =='Y':
		if i < 6 :
				ans[i] = (i+1)*dice.count(i+1)+(i+1)*2

		if i == 6: #Four of a Kind
			if dice[0] == dice[1] == dice[2]: 
				ans[i] = dice[0]*4
			elif dice[0] == dice[1] or dice[0] == dice[2]:
				ans[i] = dice[0]*4
			elif dice[1] == dice[2]:
				ans[i] = dice[1]*4
		
		if i == 7: #Full House
			if dice[0] == dice[1] == dice[2]:
				ans[i] = dice[0]*3 + 12
			elif dice[0] == dice[1]:
				ans[i] = max(dice[0]*2 + dice[2]*3, dice[0]*3 + dice[2]*2)
			elif dice[0] == dice[2]:
				ans[i] = max(dice[0]*2 + dice[1]*3, dice[0]*3 + dice[1]*2)
			elif dice[1] == dice[2]:
				ans[i] = max(dice[1]*2 + dice[0]*3, dice[1]*3 + dice[0]*2)

		if i == 8: #Little Straight
			if dice[0] != dice[1] != dice[2] and dice[0] in (1,2,3,4,5) and dice[1] in (1,2,3,4,5) and dice[2] in (1,2,3,4,5):
				ans[i] = 30
		
		if i == 9: #Big Straight
			if dice[0] != dice[1] != dice[2] and dice[0] in (2,3,4,5,6) and dice[1] in (2,3,4,5,6) and dice[2] in (2,3,4,5,6):
				ans[i] = 30

		if i == 10: #Yacht
			if dice[0] == dice[1] == dice[2]:
				ans[i] = 50

		if i == 11: #Choice
			ans[i] = sum(dice)+12

print(max(ans))



