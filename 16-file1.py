f = open('word_english.txt')
for line in f:
    line = line.rstrip()
    if line[0] == 'a' and line[-1] == 'a':
        print(line)
f.close()