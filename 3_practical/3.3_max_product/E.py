# Компилятор: Python 3.13.2
n = int(input())
a = list(map(int, input().split()))

# Списки для хранения индексов разных типов чисел
negative_indices = []
positive_indices = []
zero_indices = []

# Находим самое большое отрицательное число (ближайшее к нулю)
largest_negative_value = float('-inf')
largest_negative_index = -1

# Заполняем списки и ищем самое большое отрицательное
for i in range(n):
    if a[i] < 0:
        negative_indices.append(i)
        if a[i] > largest_negative_value:
            largest_negative_value = a[i]
            largest_negative_index = i
    elif a[i] > 0:
        positive_indices.append(i)
    else:
        zero_indices.append(i)

# Определяем, нужно ли удалять одно отрицательное число
remove_negative = len(negative_indices) % 2 == 1

# Формируем результат
result_indices = []

# Добавляем все положительные числа
result_indices.extend(positive_indices)

# Добавляем отрицательные числа, при необходимости исключая одно
for idx in negative_indices:
    if remove_negative and idx == largest_negative_index:
        continue  # Пропускаем самое большое отрицательное, если нужно удалить одно
    result_indices.append(idx)

# Особые случаи
if not result_indices:  # Если подмножество пустое
    # Если есть нули, берём один ноль
    if zero_indices:
        result_indices = [zero_indices[0]]
    # Иначе берём самый большой элемент (может быть единственным отрицательным)
    else:
        max_val = max(a)
        result_indices = [a.index(max_val)]

# Преобразуем индексы к нумерации с 1 и выводим
print(' '.join(str(i + 1) for i in result_indices))
