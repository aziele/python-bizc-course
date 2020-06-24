weight = input('Your weight [kg]: ')
height = input('Your height [m]: ')
bmi = float(weight) / float(height) ** 2
print('Your BMI: {:.1f}'.format(bmi))

if bmi > 30:
    print('Otyłość')
elif bmi >= 25 and bmi <= 29.99:
    print('Nadwaga')
elif bmi >= 18.5 and bmi <= 24.99:
    print('Waga normalna')
else:
    print('Niedowaga')