
tickets_price = 0
tickets_number = int(input('Введите количество приобретаемых билетов: '))
age_visitors = [int(input(f'{i} билет: Введите возраст посетителя: ')) for i in range(1, tickets_number + 1)]

for i_elem in age_visitors:
    if i_elem < 18:
        tickets_price += 0
    elif 25 >= i_elem >= 18:
        tickets_price += 990
    else:
        tickets_price += 1390

if tickets_number > 3:
    print(f'Общая стоимость приобретаемых билетов c учетом скидки: {tickets_price * 0.9}')
else:
    print(f'Общая стоимость приобретаемых билетов: {tickets_price}')
