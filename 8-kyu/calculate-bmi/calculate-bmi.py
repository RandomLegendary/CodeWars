def bmi(weight, height):
    number =  weight / (height ** 2)
    if number <= 18.5:
        return 'Underweight'
    elif number <= 25.0:
        return 'Normal'
    elif number <= 30.0:
        return 'Overweight'
    elif number > 30:
        return 'Obese'
​