import sys

tc = int(input())
person = []

for _ in range(tc):
    a,b = sys.stdin.readline().split()
    person.append([int(a),b])

person.sort(key=lambda x:x[0])

for i in range(len(person)):
    print("{} {}".format(person[i][0], person[i][1]))

