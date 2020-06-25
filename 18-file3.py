f = open('word_english.txt')
max_word = 'blah'
max_letters = 0
for line in f:
    line = line.rstrip()
    word_len = len(line)
    if word_len > max_letters:
        max_letters = word_len
        max_word = line 
f.close()
print(max_letters)
print(max_word)