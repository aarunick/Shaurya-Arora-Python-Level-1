print("BMI Calculator: ")
print("--------------")

weight=float(input("Enter your weight(kg) "))
height=float(input("Enter your height(meter) "))

BMI=weight/(height*height)
print("BMI: ",BMI)

if BMI<18:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("Obesity")