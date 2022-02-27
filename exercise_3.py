def check_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal"
    elif 25 >= bmi < 30:
        return "overweight"
    elif bmi >= 30:
        return "obese"


user_bmi = int(input("what is your bmi: "))
print(f"you are {check_status(user_bmi)}")

