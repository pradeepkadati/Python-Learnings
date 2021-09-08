print(" BMI Calculator")

height = float(input("Enter your height:"))
weight = int(input("Enter your weight:"))

bmi = round(weight / (height ** 2), 1)
print(f"bmi is {bmi}")
if bmi >= 35.0:
    print("Clinically Obese")
elif 35.0 > bmi >= 30.0:
    print("Obese")
elif 30.0 > bmi >= 25.0:
    print("over weight")
elif 25.0 > bmi >= 18.5:
    print("Actual Weight")
else:
    print("Under Weight")