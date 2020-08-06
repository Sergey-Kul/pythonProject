print("Ваше имя?")
name = input()
print("Привет, ", name, "!")
age = int(input("Сколько Вам полных лет? "))
height = float(input("Ваш рост? "))
weight = float(input("Ваш вес? "))
if not (not (age < 10) and not (height <= 0) and not (height > 3) and not (weight <= 0) and not (weight > 500)):
    print('ошибочные данные')
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)
    print("Ваш индекс массы тела: ", bmi)
    if bmi < 18.5:
        description = "недостаточной массой тела"
    elif bmi < 25:
        description = "нормальной массой тела"
    elif bmi < 30:
        description = "избыточной массой тела"
    else:
        description = "ожирением"
    print("вы относитесь к группе людей с", description)