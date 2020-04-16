def user(*args):
    return args

name = input('Введите имя')
surname = input('Введите фамилию')
was_born = input('Введите год рожения')
city = input('Введите город')
email = input('Введите емейл')
phone = input('Введите телефон')

print(user(name, surname, was_born, city, email, phone))
