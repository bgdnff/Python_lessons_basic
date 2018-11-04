# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    if n<1 or n>m :
        return []
    fib_list = []
    fib1 = 0
    fib2 = 1
    fib = 1
    i=2
    if n ==1:
        fib_list.append(1)
    while i <= m:
        if i >= n:
            fib_list.append(fib)
        fib1 = fib2
        fib2 = fib
        fib = fib1+fib2
        i += 1
    return fib_list

print(fibonacci(5,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
        start = 0
        end = len(origin_list)-1
        while end > start:
            current = start
            while current < end:
                if origin_list[current] > origin_list[current+1]:
                    temp = origin_list[current]
                    origin_list[current] = origin_list[current+1]
                    origin_list[current+1] = temp
                current = current +1
            end -=1

        return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print(sort_to_max([2]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def plusone(li):
    return li + 1
def my_filter(func, list):
    result_list = []
    for i in list:
        if func(i):
            result_list.append(i)
    return result_list

print(my_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14]))
print(my_filter(plusone, [-1, 7, 3, -6, 4, 0, 5]))
print(my_filter(len, ['', 'not null', 'bla', '', '10']))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):
    f1 = x1-x2 == x3-x4 and y1-y2 == y3-y4
    f2 = x1-x2 == x4-x3 and y1-y2 == y4-y3

    f3 = x1-x3 == x4-x2 and y1-y3 == y4-y2
    f4 = x1-x3 == -(x4-x2) and y1-y3 == -(y4-y2)
    return f1 or f2 or f3 or f4
print(is_parallelogram(0,0,2,5,1,1,1,4))
