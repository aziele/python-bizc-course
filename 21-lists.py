lst = []
for i in range(0, 4):
    word = input('Enter a word: ')
    lst.append(word)

lst.sort()
for word in lst:
    print(word)