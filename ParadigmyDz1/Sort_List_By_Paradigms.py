from random import randint

# Императивная парадигма
def insert_sort(arr): # Сортировка встакой
    n_el = len(arr) 
    for i in range(n_el - 1): # Проходим по всем эл-там списка
        m = i                 # Создаем временную переменную
        for j in range(i + 1, n_el): # Берем значение второго с края э-та
            if arr[j] > arr[m]: # Если значение, больше предыдущего
                m = j           # Сохраняем во временную переменную
        arr[i], arr[m] = arr[m], arr[i]  # Меняем значения э-тов местами            
    return arr


# Декларативная парадигма
def declarate_sort(arr: [int]):   #  Объявляем ф-цию  
    return (sorted(arr, reverse=True)) # Применяем метод sorted() с параметром разворота reverse=True


arr = [randint(0, 1000) for _ in range(20)] # "Генерируем случайный несортированный список целых чисел"
print("Несортированный список")
print(arr)
print("Cортированные по убыванию списки")
print(insert_sort(arr))
print(declarate_sort(arr))