# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

#  здесь ваш код

import room_1
import room_2

print('В комнате room_1 живут: ', end='')
print(','.join(room_1.folks))
print('В комнате room_2 живут: ', end='')
print(','.join(room_2.folks))

# Зачёт!
