

def row(sel1, sel2, sel3):      # Отрисовка верхних рядов таблицы
    print('\t    |    |    ')
    print('\t  {} |  {} |  {} '.format(sel1, sel2, sel3))
    print('\t____|____|____')

def row_low(sel1, sel2, sel3):  # Отрисовка нижнего ряда таблицы
    print('\t    |    |    ')
    print('\t  {} |  {} |  {} '.format(sel1, sel2, sel3))
    print('\t    |    |    ')

def matrix2(MTRIX):             # Отрисовка таблицы
    print('\n')
    row(MTRIX[0], MTRIX[1], MTRIX[2])
    row(MTRIX[3], MTRIX[4], MTRIX[5])
    row_low(MTRIX[6], MTRIX[7], MTRIX[8])
    print('\n')