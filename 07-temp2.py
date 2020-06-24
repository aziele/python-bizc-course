number = input('Enter a number: ')
number = float(number)
if number > 0 and number <= 10:
    results = "The number greater than 0 and lower than 10"
elif number < 0:
    result = "The number smaller than 0."
else:
    result = "The number is 0."
print(result)
