height = float(input())

weight = int(input())

bmi = (float(weight) / pow(float(height), 2))
result_bmi = "you are underweight." if bmi < 18.5 else "you are normal weight." if bmi > 18.5 and bmi < 25 else "you are slightly overweight." if bmi > 25 and bmi < 30 else "you are obese." if bmi > 30 and bmi < 35 else "ypur are clinically obese."

print(f'Your BMI is {bmi:.2f}, {result_bmi}')