from veiw import matrix2


def game(): # Ф-ция обработки логики игры

    MTRIX = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Список ячеек
    step_count = 0                    # Счетчик ходов
    win_status = False                # Статус выгирыша
    win_lst = '123_456_789_147_258_369_159_357'  # Строка выигрышных комбинаций
    
    print('Кто ходит первым ?\nЕсли игру начинает X, то введите цифру: 1\nЕсли игру начинает O, то введите цифру: 0\n')
    plyer = get_plyer_input()
    while not win_status:  # Пока никто не выграл
            matrix2(MTRIX)        #  Отрисовка таблицы
            if plyer == 1: plyer = 0   #  Переход хода
            else:
                plyer = 1
            if step_count == 9:  # Все ячейки заняты, но никто не выиграл        
                print('НИЧЬЯ')
                break
            step_count += 1      # Счетчик ходов + ход
            
            if plyer == 0:                    
                point = get_pointX_input()    
                if point not in MTRIX:  # Если в списке нет номера ячейки - воврат к выбру
                    print('Место занято - выбирете свободный номер ячейки\\n ') #
                    continue
                win_lst = win_lst.replace(str(point), 'X') # Иначе заменяем в строке выигрышных комбинаций число на символ игрока      
                for x in range(9):  # В списке ячеек меняем номер ячейки на символ игрока (выбрать его будет невозможно)
                    if MTRIX[x] == point: MTRIX[x] = 'X'
                if 'XXX' in win_lst:  # Если в строке выигрышных комбинаций есть ХХХ, то называем победителя и прерываем выполнение программы
                    matrix2(MTRIX)
                    print('ИГРОК X ВЫИГРАЛ!')
                    break

            if plyer == 1:  # Те же операции для втрого игрока 
                point = get_pointO_input() 
                if point not in MTRIX:
                    print(f'Место занято - выбирете свободный номер ячейки\n ')
                    continue          
                win_lst = win_lst.replace(str(point), '0')
                for x in range(9): 
                    if MTRIX[x] == point: MTRIX[x] = '0'
                if '000' in win_lst:
                    matrix2(MTRIX)
                    print('ИГРОК 0 ВЫИГРАЛ!')
                    break           
    exit() # Выход из программы

def get_plyer_input(): # Ф-ция обработки ошибки ввода
    while True:
        try:
            return int(input("Введите цифру 1 или 0, Вашвыбор:  "))
        except ValueError:
            print("Ошибка ввода. Нажали что-то не то!")

def get_pointX_input():  # Ф-ция обработки ошибки ввода
        try:
            return int(input('Ход игрока X - выбирете номер ячейки \n '))
        except ValueError:
            print("Ошибка ввода. Нажали что-то не то!")

def get_pointO_input():   # Ф-ция обработки ошибки ввода
    while True:
        try:
            return int(input('Ход игрока 0 - выбирете номер ячейки \n '))
        except ValueError:
            print("Ошибка ввода. Нажали что-то не то!")
