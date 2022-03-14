# -*- coding: utf-8 -*-

import simple_draw as sd

from package_village import branch_1
from package_village import branch_2
from package_village import house
from package_village import smile
from package_village.rainbow import rainbow_colors
from package_village.snow import snow_1
from package_village.sun import sun

sd.background_color = (255, 248, 220)
sd.resolution = (1200, 600)


# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

def house_village():
    print(house)
    print(smile)
    print(branch_1)
    print(branch_2)


while True:
    sd.start_drawing()
    sun()
    rainbow_colors()
    snow_1()
    sd.finish_drawing()
    if sd.user_want_exit():
        break

house_village()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# Зачёт!
