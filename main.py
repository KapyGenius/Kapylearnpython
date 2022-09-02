weight = int(input("What is your weight? "))
height = float (input("What is your height? "))

bmi = weight / (height**2)
bmi = int(bmi)

print(f"Ton BMI est {bmi}.")
print(f"your weight is {weight} kg and your height is {height}m.")