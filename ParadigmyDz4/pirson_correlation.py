from typing import List

# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# Формула корреляции Пирсона
# Rxy = SUM(Xi - Mx)*(Yi - My)/(SUM((Xi - Mx)^2)*((Yi - My)^2))^0.5

def correlation_calculation(arr_X: List[float], arr_Y: List[float]):

# Расчитатать корреляцию по формуле можно только для одинаковых массивов по к-ву эл-тов
    if len(arr_X) != len(arr_Y):
        raise ValueError("Ожидаетюся массивы с одинаковым количеством элементов")
    
    n = len(arr_X) # Переменная к-ва эл-тов массива

    average_value_X = sum(arr_X) / n # среднее арифметическое для arr_X - Mx
    average_value_Y = sum(arr_Y) / n # среднее арифметическое для arr_Y - My

# Произведение сумм отклонения от среднего X и Y - SUM(Xi - Mx)*(Yi - My)
    average_deviation = sum(((arr_X[i] - average_value_X) * (arr_Y[i] - average_value_Y)) for i in range(n))
    

# Отклонение от среднего квадратичного X и Y - (SUM((Xi - Mx)^2)*((Yi - My)^2))^0.5
    quadratic_deviation_X = sum((arr_X[i] - average_value_X) ** 2 for i in range(n))
    quadratic_deviation_Y = sum((arr_Y[i] - average_value_Y) ** 2 for i in range(n))
    quadratic_deviation = (quadratic_deviation_X  * quadratic_deviation_Y) ** 0.5
    

# Корреляции массивов Пирсона
    pirson_correlation = average_deviation / quadratic_deviation
    return pirson_correlation



arr_X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#arr_Y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
arr_Y = [0, 25, 68, 8, 57, 100, 84, 11, 44, 57]

print(f"Корреляция Пирсона: {correlation_calculation(arr_X, arr_Y)}") 