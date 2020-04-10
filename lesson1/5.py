revenue = input('Inpput revenue: ')
costs = input('Inpput costs: ')
rentability = int(revenue) - int(costs)
if int(revenue) > int(costs):
    print(f'прибыль, заработано {rentability}')
else:
    print('убыток')

workers = input('amount of workers: ')
print('каждый сотрудник заработал: ', rentability / int(workers))