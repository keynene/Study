tc = int(input())

word = [input() for _ in range(tc)]

set_word = set(word)
word = list(set_word)

word.sort()
word.sort(key=len)
for i in word:
    print(i)