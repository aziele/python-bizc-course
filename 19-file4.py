f = open('word_english.txt')
max_letters = 0
for line in f:
    line = line.rstrip()
    word_len = len(line)
    if word_len > max_letters:
        max_letters = word_len
f.close()

f = open('word_english.txt')
for line in f:
    word = line.rstrip()
    if len(word) == max_letters:
        print('Longest word: {}'.format(word))


