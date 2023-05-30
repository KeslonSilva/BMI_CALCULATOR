height = float(input('enter your height in m: '))
weight = float(input('enter your weight in kg: '))
bmi = round(height / weight ** 2)
print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underwheight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal wheight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overwheight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")