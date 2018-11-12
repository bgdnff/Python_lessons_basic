# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
new_dir = list('dir_{}'.format(i) for i in range(1,10))
for d in new_dir:
    try:
       os.mkdir(d)
    except FileExistsError:
        pass # просто промолчим
        # print(d,' уже существует')

del_dir =  list('dir_{}'.format(i) for i in range(1,10))
for d in del_dir:
    try:
        pass #os.rmdir(d)
    except FileNotFoundError:
        pass  # просто промолчим
        # print(d,' нет такого')



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print(list(filter(os.path.isdir, os.listdir())))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт
