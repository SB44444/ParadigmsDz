from controller import game
import os

clear = lambda: os.system('cls') # Очиста терминала
clear()
# os.system('cls')

def main(): # Функция запуска
    game() # Функция старта основной программы

if __name__ == '__main__':   # Проверка имени функции запуска программы
    main()