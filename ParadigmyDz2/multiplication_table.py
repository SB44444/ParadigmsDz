

def multiplication_table(n):
    
    for i in range(1, n+1):
        for j in range(1, 10):
            print(f'{j}  *  {i}  =  {i * j}')
        print()    


n = input('Введите целое число n, Ваш ввод:  ')
try:
    n = int(n)
    print(f"\nТаблицаа умножения на {n}: \n")
    multiplication_table(n)
except:
    print(f"Ошибка ввода. Нажали что-то не то - {n} не целое число")
