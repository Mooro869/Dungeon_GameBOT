from aiogram import types

# Кнопки при запуске бота
keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
info_button = types.KeyboardButton('Информацияℹ️')
start_game = types.KeyboardButton('Начать игру🎮')
statistic_button = types.KeyboardButton('Статистика📋')
keyb.add(start_game, statistic_button, info_button)

# Кнопки персонажей
persons_button = types.InlineKeyboardMarkup(row_width=2)
wizard = types.KeyboardButton("Волшебник🧙‍♂️", callback_data="wizard")
knight = types.KeyboardButton("Рыцарь⚔️", callback_data="knight")
persons_button.add(wizard, knight)

'''
ОСНОВНЫЕ КНОПКИ ДЛЯ КАЖДОЙ ДВЕРИ
ВОЛШЕБНИКА
'''

# Основные кнопки 1_1
wizard_battle1_1 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack1_1 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack1_1')
wizard_away1_1 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away1_1')
wizard_battle1_1.add(wizard_attack1_1, wizard_away1_1)

# Основные кнопки 1_2
wizard_battle1_2 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack1_2 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack1_2')
wizard_away1_2 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away1_2')
wizard_battle1_2.add(wizard_attack1_2, wizard_away1_2)

# Основные кнопки 2_1
wizard_battle2_1 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack2_1 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack2_1')
wizard_away2_1 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away2_1')
wizard_battle2_1.add(wizard_attack2_1, wizard_away2_1)

# Основные кнопки 2_2
wizard_battle2_2 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack2_2 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack2_2')
wizard_away2_2 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away2_2')
wizard_battle2_2.add(wizard_attack2_2, wizard_away2_2)

# Основные кнопки 3_1
wizard_battle3_1 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack3_1 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack3_1')
wizard_away3_1 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away3_1')
wizard_battle3_1.add(wizard_attack3_1, wizard_away3_1)

# Основные кнопки 3_2
wizard_battle3_2 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack3_2 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack3_2')
wizard_away3_2 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away3_2')
wizard_battle3_2.add(wizard_attack3_2, wizard_away3_2)

# Основные кнопки 4_1
wizard_battle4_1 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack4_1 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack4_1')
wizard_away4_1 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away4_1')
wizard_battle4_1.add(wizard_attack4_1, wizard_away4_1)

# Основные кнопки 4_2
wizard_battle4_2 = types.InlineKeyboardMarkup(row_width=2)
wizard_attack4_2 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack4_2')
wizard_away4_2 = types.KeyboardButton('Сбежать🏃', callback_data='wizard_away4_2')
wizard_battle4_2.add(wizard_attack4_2, wizard_away4_2)

# Основные кнопки 5
wizard_battle5 = types.InlineKeyboardMarkup(row_width=1)
wizard_attack5 = types.KeyboardButton('Атаковать👊', callback_data='wizard_attack5')
wizard_battle5.add(wizard_attack5)  # будет только кнопка атаки, так как сражение против босса

'''
ОСНОВНЫЕ КНОПКИ ДЛЯ КАЖДОЙ ДВЕРИ
РЫЦАРЬ
'''

# Основные кнопки 1_1
knight_battle1_1 = types.InlineKeyboardMarkup(row_width=2)
knight_attack1_1 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack1_1')
knight_away1_1 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away1_1')
knight_battle1_1.add(knight_attack1_1, knight_away1_1)

# Основные кнопки 1_2
knight_battle1_2 = types.InlineKeyboardMarkup(row_width=2)
knight_attack1_2 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack1_2')
knight_away1_2 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away1_2')
knight_battle1_2.add(knight_attack1_2, knight_away1_2)

# Основные кнопки 2_1
knight_battle2_1 = types.InlineKeyboardMarkup(row_width=2)
knight_attack2_1 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack2_1')
knight_away2_1 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away2_1')
knight_battle2_1.add(knight_attack2_1, knight_away2_1)

# Основные кнопки 2_2
knight_battle2_2 = types.InlineKeyboardMarkup(row_width=2)
knight_attack2_2 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack2_2')
knight_away2_2 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away2_2')
knight_battle2_2.add(knight_attack2_2, knight_away2_2)

# Основные кнопки 3_1
knight_battle3_1 = types.InlineKeyboardMarkup(row_width=2)
knight_attack3_1 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack3_1')
knight_away3_1 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away3_1')
knight_battle3_1.add(knight_attack3_1, knight_away3_1)

# Основные кнопки 3_2
knight_battle3_2 = types.InlineKeyboardMarkup(row_width=2)
knight_attack3_2 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack3_2')
knight_away3_2 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away3_2')
knight_battle3_2.add(knight_attack3_2, knight_away3_2)

# Основные кнопки 4_1
knight_battle4_1 = types.InlineKeyboardMarkup(row_width=2)
knight_attack4_1 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack4_1')
knight_away4_1 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away4_1')
knight_battle4_1.add(knight_attack4_1, knight_away4_1)

# Основные кнопки 4_2
knight_battle4_2 = types.InlineKeyboardMarkup(row_width=2)
knight_attack4_2 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack4_2')
knight_away4_2 = types.KeyboardButton('Сбежать🏃', callback_data='knight_away4_2')
knight_battle4_2.add(knight_attack4_2, knight_away4_2)

# Основные кнопки 5
knight_battle5 = types.InlineKeyboardMarkup(row_width=1)
knight_attack5 = types.KeyboardButton('Атаковать👊', callback_data='knight_attack5')
knight_battle5.add(knight_attack5)  # будет только кнопка атаки, так как сражение против босса

'''
КНОПКИ ДВЕРЕЙ
ВОЛШЕБНИКА
'''

# Двери 1 комната
wizard_doors1 = types.InlineKeyboardMarkup(row_width=2)
wizard_door1_1_1 = types.KeyboardButton('Первая дверь🚪', callback_data='wizard_door1_1')
wizard_door2_1_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='wizard_door1_2')
wizard_doors1.add(wizard_door1_1_1, wizard_door2_1_2)

# Двери 2 комната
wizard_doors2 = types.InlineKeyboardMarkup(row_width=2)
wizard_door1_2_1 = types.KeyboardButton('Первая дверь🚪', callback_data='wizard_door2_1')
wizard_door2_2_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='wizard_door2_2')
wizard_doors2.add(wizard_door1_2_1, wizard_door2_2_2)

# Двери 3 комната
wizard_doors3 = types.InlineKeyboardMarkup(row_width=2)
wizard_door1_3_1 = types.KeyboardButton('Первая дверь🚪', callback_data='wizard_door3_1')
wizard_door2_3_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='wizard_door3_2')
wizard_doors3.add(wizard_door1_3_1, wizard_door2_3_2)

# Двери 4 комната
wizard_doors4 = types.InlineKeyboardMarkup(row_width=2)
wizard_door1_4_1 = types.KeyboardButton('Первая дверь🚪', callback_data='wizard_door4_1')
wizard_door2_4_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='wizard_door4_2')
wizard_doors4.add(wizard_door1_4_1, wizard_door2_4_2)

# Двери 5 комната
wizard_doors5 = types.InlineKeyboardMarkup(row_width=2)
wizard_door5 = types.KeyboardButton('Финальная дверь🚪', callback_data='wizard_door5')
wizard_doors5.add(wizard_door5)

'''
КНОПКИ ДВЕРЕЙ
РЫЦАРЯ
'''

# Двери 1 комната
knight_doors1 = types.InlineKeyboardMarkup(row_width=2)
knight_door1_1_1 = types.KeyboardButton('Первая дверь🚪', callback_data='knight_door1_1')
knight_door2_1_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='knight_door1_2')
knight_doors1.add(knight_door1_1_1, knight_door2_1_2)

# Двери 2 комната
knight_doors2 = types.InlineKeyboardMarkup(row_width=2)
knight_door1_2_1 = types.KeyboardButton('Первая дверь🚪', callback_data='knight_door2_1')
knight_door2_2_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='knight_door2_2')
knight_doors2.add(knight_door1_2_1, knight_door2_2_2)

# Двери 3 комната
knight_doors3 = types.InlineKeyboardMarkup(row_width=2)
knight_door1_3_1 = types.KeyboardButton('Первая дверь🚪', callback_data='knight_door3_1')
knight_door2_3_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='knight_door3_2')
knight_doors3.add(knight_door1_3_1, knight_door2_3_2)

# Двери 4 комната
knight_doors4 = types.InlineKeyboardMarkup(row_width=2)
knight_door1_4_1 = types.KeyboardButton('Первая дверь🚪', callback_data='knight_door4_1')
knight_door2_4_2 = types.KeyboardButton('Вторая дверь🚪', callback_data='knight_door4_2')
knight_doors4.add(knight_door1_4_1, knight_door2_4_2)

# Двери 5 комната
knight_doors5 = types.InlineKeyboardMarkup(row_width=2)
knight_door5 = types.KeyboardButton('Финальная дверь🚪', callback_data='knight_door5')
knight_doors5.add(knight_door5)
