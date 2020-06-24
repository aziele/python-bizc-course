weight = input('Your weight [kg]: ')
height = input('Your height [m]: ')
bmi = float(weight) / float(height) ** 2
print('Your BMI: {:.1f}'.format(bmi))