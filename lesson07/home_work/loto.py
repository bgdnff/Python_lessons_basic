#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random



class Card:
    def __init__(self, player):
        self.player = player
        self.checked = 0
        self.allnumbers = set()
        random.seed()
        while len(self.allnumbers)<15:
            self.allnumbers.add(random.randint(1, 90))
        self.allnumbers = list(self.allnumbers)
        random.shuffle(self.allnumbers)
        self.lines = []
        self.lines.append(list(self.allnumbers)[:5])
        self.lines.append(list(self.allnumbers)[5:10])
        self.lines.append(list(self.allnumbers)[10:])
        self.lines[0].sort()
        self.lines[1].sort()
        self.lines[2].sort()
        for i in range(4):
            self.lines[0].insert(random.randint(0,5+i),'  ')
            self.lines[1].insert(random.randint(0,5+i),'  ')
            self.lines[2].insert(random.randint(0,5+i),'  ')

    def print_card(self):
        print('{:-^26}'.format(' '+self.player+' '))
        str=''
        for l in self.lines:
            print(str.join(['{: >2} '.format(i) for i in l]))
        print('{:-^26}'.format(''))

    def check_barrel(self, barrel):
        for line in self.lines:
            if line.count(barrel):
                line[line.index(barrel)] = '--'
                self.checked +=1
                return True

        return False




used = []
players = [Card('Player'),  Card('Computer')]
wins = [False,False]
while not(wins[0]or wins[1]):
    bar = random.randint(1, 90)
    while bar in used:
        bar = random.randint(1, 90)
    used.append(bar)
    print('выпал бочонок: {} (осталось {})'.format(bar,90-len(used)))
    for p in players:
        p.print_card()
    choice = ''
    while choice not in ('y','n'):
        choice=input('Зачеркнуть цифру? (y/n)')
    check = players[0].check_barrel(bar)
    if (choice == 'y')== check :
        wins[0] = (players[0].checked == 15)
        # компьютер слегка читерит :)
        print('компьютер зачеркивает' if players[1].check_barrel(bar) else 'компьютер пропускает ход')
        wins[1] = (players[1].checked == 15)
    else:
        wins[1] = True

print('Вы победили!' if wins[0] else 'Вы проиграли')