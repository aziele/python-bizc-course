f = open('word_english.txt')
num_lines = 0
for line in f:
    line = line.rstrip()
    if line == line[::-1] and len(line) > 3:
        num_lines += 1
        print(line)
f.close()
print('Number of palindromes: {}'.format(num_lines))