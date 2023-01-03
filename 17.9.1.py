

def check_list():

    try:
        sequence = list(map(int, input('Введите последовательность целых чисел через пробел: ').split()))
    except ValueError:
        print('Не корректный ввод.')
        return check_list()
    else:
        return sequence


def check_number():

    numb = input('Введите целое число относительно которого будем искать элементы: ')
    if numb.isdigit():
        return numb
    else:
        print('Не корректный ввод.')
        return check_number()


def quick_sort(initial_list):

    if len(initial_list) <= 1:
        return initial_list
    elem = initial_list[0]
    left_part = [i for i in initial_list if i < elem]
    center_part = [i for i in initial_list if i == elem]
    right_part = [i for i in initial_list if i > elem]
    return quick_sort(left_part) + center_part + quick_sort(right_part)


def binary_search(array, element, left, right):

    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


sequence_of_numbers = check_list()
number = int(check_number())
sorted_list = quick_sort(sequence_of_numbers)

print(f'Отсортированный по возрастанию список элементов {sorted_list}')

limit_left = 0
limit_right = len(sorted_list) - 1
index = binary_search(sorted_list, number, limit_left, limit_right)

previous_index = index - 1
while sorted_list[previous_index] == sorted_list[index]: # ищем индекс первого меньшего числа. актуально для списков
    previous_index -= 1                                  # с повторяющимися элементами

if index:
    print(f'Индекс искомого элемента {index}\nИндекс предшествующего меньшего элемента'
          f' {previous_index}\nИндекс следующего большего или равного элемента {index + 1}')
else:
    print(f'Элемент {number} отсутствует в списке элементов {sorted_list}')
