
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую хотите положить в банк: '))
deposit = []

for i_elem in per_cent.values():                            # через цикл проще, чем 4 раза расписывать
    deposit.append(int(i_elem * money / 100))               # deposit.append(per_cent['ТКБ'] * money / 100)
                                                            # deposit.append(per_cent['СКБ'] * money / 100)
print(f'\nСумма накопленных средств составит: {deposit}')
print(f'\nМаксимальная сумма, которую Вы можете заработать: {max(deposit)}')


# а так еще симпатичнее выглядит:)
print('\nСумма накопленных средств за год составит:')
for key, value in per_cent.items():
    print(f'Банк {key} - сумма накоплений {value * money / 100}')
