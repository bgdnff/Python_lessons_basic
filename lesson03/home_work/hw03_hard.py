# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
parser = []
def NOK(a,b):
    while a%b :
        temp = a%b
        a=b
        b=temp
    return b

# print(NOK(1,42))

def getnext(i, str):
    print(i,str)
    #nonlocal fr_str, str
    if i == -1:
        print(str, '!', str)
        return [str,str]
    else:
        substr = str[:i]
        str = str[i+1:]
        print(substr,'!', str)
        return [substr,str]

def read_fraction():
    fraction={'sig':1, 'whole':0, 'numerator':0, 'denomerator':1}
    global parser
    i=0
    #parser = ["",fr_str]

    if parser[1][i]== '-':
        fraction['sig'] = -1
        i+=1
    parser = ['', parser[1][i:]]
    parser = getnext(parser[1].find(' '), parser[1])

    if parser[0].find('/') == -1:
        fraction['whole'] = int(parser[0])
        parser = getnext(parser[1].find(' '), parser[1])
    fraction['numerator'] = int(parser[0][:parser[0].find('/')])
    fraction['denomerator'] = int(parser[0][parser[0].find('/')+1:])
    return fraction

def twofractions(str):
    def unregular_numer(fract):
        return int(fract['sig']*(fract['whole']*fract['denomerator']+fract['numerator']))
    global parser
    parser = ['',str]
    fract1 = []
    fract2 = []
    fract1 = read_fraction()
    parser = getnext(parser[1].find(' '),parser[1])
    sign = parser[0]
    fract2 = read_fraction()
    print(fract1)
    print(fract2)
    if sign == '-':
        fract2['sig'] *=-1

    numer = unregular_numer(fract1)*fract2['denomerator']+unregular_numer(fract2)*fract1['denomerator']
    print(unregular_numer(fract1),unregular_numer(fract2))
    den = fract1['denomerator']*fract2['denomerator']
    result_fr={'sig':1, 'whole':0, 'numerator':0, 'denomerator':1}
    if numer < 0:
        result_fr['sig'] = -1
        numer*=-1
    result_fr['whole'] = numer//den
    numer = numer%den

    nok = NOK(numer,den)

    result_fr['numerator'] = numer//nok
    result_fr['denomerator'] = den//nok
    res_str = ''
    if result_fr['sig']<0:
        res_str='-'

    if result_fr['whole']!=0:
        res_str+='{} '.format(result_fr['whole'])
    if result_fr['numerator']!=0:
        res_str+='{}/{}'.format(result_fr['numerator'], result_fr['denomerator'])
    return res_str



print(twofractions('-1 2/3 + -1 4/6'))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
