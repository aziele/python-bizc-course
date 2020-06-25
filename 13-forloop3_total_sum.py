number = input('Enter an integer number: ')
number = int(number)

total_sum = 0
for i in range(number + 1):
    total_sum += i
    # total_sum = total_sum + i
print('Sum: {}'.format(total_sum))