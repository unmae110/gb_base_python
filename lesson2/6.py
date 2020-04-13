next_enter = True
counter = 1
product_list = []

product_template = {
    'название': ('Имя товара', str),
    'цена': ('Стоимость', int),
    'кол-во': ('Кол-во', int),
    'ед': ('Ед измерения (шт, кг, л)', str)
}

while next_enter:
    product = {}
    for key, value in product_template.items():
        while True:
            user_input = input(f'{value[0]}\n')
            product[key] = user_input
            break
    product_list.append((counter, product))
    counter += 1
    next_product = input("Еще товар? ")
    if next_product.lower() not in ("y", "да"):
        next_enter = False
        break
print(product_list)
