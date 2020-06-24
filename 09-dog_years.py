age = input("Enter a dog's age in human years: ")
age = float(age) # Convert string to float.
if age <= 2:
    result = age * 10.5
else:
    result = 21 + (age-2)*4
print("Dog's age in dog's years: {}".format(result))