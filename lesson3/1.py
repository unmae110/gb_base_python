def func(a,b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return "Делить на ноль нельзя"
    except ValueError:
        return "Введите число"

num1 = input("Num1: ")
num2 = input("Num2: ")
print(func(num1,num2))