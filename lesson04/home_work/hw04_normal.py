import re
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# c RE

# этот вариант подходит для предложенной строки(состоит только из больших и маленьких букв),
# но не для общего случая
print(re.split('[A-Z]+', line))

#### без RE

# Есть несколько способов: с использованием for ch in line, но тогда придется собирать подстроки посимвольно
# можно получать подстроки через срезы, но тогда нужно проходить строку с помощью индексов,
# наконец, можно получать индексы с помощью enumerate, но тогда создается список,
# где к каждому символу из строки припишется номер - т.е. вдвое бльший размер
# и дополнитеьный проход по строке, что тоже нехорошо.

i = 0
started = False
result = []
for i in range(len(line)):
    if started:
        if line[i].isupper():               # если отслеживали подстроку и встретили верхний регистр
            result.append(line[start:i])    # то записываем ее в результат
            started = False                 # и заканчиваем отслеживание
    else:
        if line[i].islower():               # если еще не начали отслеживать подстроку из малых букв,
                start = i                   # то начинаем
                started = True


if started:                                 # если осталась незаконченая строка, записываем ее в результат
    result.append(line[start:])

print(result)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

pattern = '[a-z]{2}([A-Z]+)[A-Z]{2}'
print(re.findall(pattern, line_2))


# без re
lows = 0
ups = 0
result2 = []

for i in range(len(line_2)):
    if line_2[i].isupper():                             # если большой - считаем его
        ups += 1
    else:
        if ups:                                         # попали на малыйсимвол после большого (ups>0)
            if ups > 2 and lows >= 2:                   # и больших было больше двух, а до них малых не меньше 2
                result2.append(line_2[i-ups:i-2])       # то это то что нам нужно!

            ups = 0                                     # сбрасываем сетчики
            lows = 1                                    # один малый мы читаем как раз сейчас
        else:
            lows +=1                                    # если малый после малого, просто увеличиваем счетчик

# опять проверяем конец строки
if ups > 2 and lows >= 2:
    result2.append(line_2[i-ups:i-2])



print(result2)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os, random

def fillfile(filename):
    with open(filename, 'w', encoding='UTF-8') as f:
        for i in range(2500):
            f.write(str(random.randint(0, 9)))

file = 'longnumber.txt'

#fillfile(file)
with open(file, 'r', encoding='UTF-8') as f:
    long_line = f.readline()


maxline = 0
maxchar = ''
curr = 0
prev = ''

# перебираем все символы в строке и сравниваем с предыдущим,
# если совпадают, увеличиваем счетчик, если нет - сбрасываем счетчик
for ch in long_line:
    if ch is prev:
        curr +=1
    else:
        if maxline<curr:
            maxline = curr
            maxchar = prev
        curr=1
    prev = ch
print(maxchar*maxline)
