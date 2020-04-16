def my_func(arg1, arg2, arg3):
    if int(arg1) < int(arg2):
        arg1 = arg2
    elif int(arg3) < int(arg2):
        arg3 = arg2
    return int(arg1) + int(arg3)


num1 = input('num1:')
num2 = input('num2:')
num3 = input('num3:')

print(my_func(num1, num2, num3))