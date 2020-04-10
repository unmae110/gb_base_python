seconds = input('Введите время в секундах: ')
hours = int(seconds) // 3600
minutes = int(seconds) // 60
print(f'{hours}:{minutes}:{seconds}')