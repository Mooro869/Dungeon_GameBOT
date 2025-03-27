import time
import random
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram import executor

import config
import keyboard as kb

# @Dungeon_GameBot
bot = Bot(token=config.TOKEN_API)
# bot = Bot(token=config.TOKEN_API, proxy='http://10.0.48.52:3128')
dp = Dispatcher(bot=bot)


# ОСНОВНЫЕ КНОПКИ
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=config.START_TEXT, reply_markup=kb.keyb)


@dp.message_handler(text=['Информацияℹ️'])
async def information_command(message: types.Message):
    await message.answer(text=config.INFORMATION_TEXT)


@dp.message_handler(text=['Начать игру🎮'])
async def start_command(message: types.Message):
    config.wizard['hp'] = config.HP_WIZARD
    config.knight['hp'] = config.HP_KNIGHT
    await message.answer(text=config.START_GAME_TEXT, reply_markup=kb.persons_button)


# ВОЛШЕБНИК
@dp.callback_query_handler(lambda x: x.data == "wizard")
async def wizard_delete_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.WIZARD_HISTORY)
    # Вывод дверных кнопок 1 комнаты
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.WIZARD_START_TEXT,
                           reply_markup=kb.wizard_doors1)


'''
Функции вывода кнопок ВОЛШЕБНКА
'''


# 1_1 Паук
@dp.callback_query_handler(lambda x: x.data == "wizard_door1_1")
async def wizard_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.wizard_battle1_1)


# 1_2 Слайм

@dp.callback_query_handler(lambda x: x.data == "wizard_door1_2")
async def wizard_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.wizard_battle1_2)


# 2_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "wizard_door2_1")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.wizard_battle2_1)


# 2_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "wizard_door2_2")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.wizard_battle2_2)


# 3_1 Голем
@dp.callback_query_handler(lambda x: x.data == "wizard_door3_1")
async def wizard_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.GOLEM_MEETING,
                           reply_markup=kb.wizard_battle3_1)


# 3_2 Паук
@dp.callback_query_handler(lambda x: x.data == "wizard_door3_2")
async def wizard_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.wizard_battle3_2)


# 4_1 Паук
@dp.callback_query_handler(lambda x: x.data == "wizard_door4_1")
async def wizard_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.wizard_battle4_1)


# 4_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "wizard_door4_2")
async def wizard_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.wizard_battle4_2)


# 5 Демон
@dp.callback_query_handler(lambda x: x.data == "wizard_door5")
async def wizard_room5_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    config.wizard['hp'] += 15
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.BONUS_HP + str(config.wizard['hp']))
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.DEMON_MEETING,
                           reply_markup=kb.wizard_battle5)


'''
Функции атаки волшебника
'''


# Действия при атаке 1_1
@dp.callback_query_handler(lambda x: x.data == "wizard_attack1_1")
async def wizard1_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= sp_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            break
        elif config.wizard['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                   reply_markup=kb.wizard_doors2)
            break


# Действия при атаке 1_2
@dp.callback_query_handler(lambda x: x.data == "wizard_attack1_2")
async def wizard1_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sl_push = random.randint(1, config.slime['pw'])
        config.slime['hp'] -= w_push
        config.wizard['hp'] -= sl_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье слайму после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            await dp.wait_closed()
            break
        elif config.wizard['hp'] >= 1:
            config.slime['hp'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)

            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                   reply_markup=kb.wizard_doors2)
            break


# Действия при атаке 2_1
@dp.callback_query_handler(lambda x: x.data == "wizard_attack2_1")
async def wizard2_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sl_push = random.randint(1, config.slime['pw'])
        config.slime['hp'] -= w_push
        config.wizard['hp'] -= sl_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье слайму после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            await dp.wait_closed()
            break
        elif config.wizard['hp'] >= 1:
            config.slime['hp'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                   reply_markup=kb.wizard_doors3)
            break


# Действия при атаке 2_2
@dp.callback_query_handler(lambda x: x.data == "wizard_attack2_2")
async def wizard2_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sk_push = random.randint(1, config.skeleton['pw'])
        config.skeleton['hp'] -= w_push
        config.wizard['hp'] -= sk_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье скелету после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            await dp.wait_closed()
            break
        elif config.wizard['hp'] >= 1:
            config.skeleton['hp'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                   reply_markup=kb.wizard_doors3)
            break


# Действия при атаке 3_1
@dp.callback_query_handler(lambda x: x.data == "wizard_attack3_1")
async def wizard3_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.golem['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        g_push = random.randint(1, config.golem['pw'])
        config.golem['hp'] -= w_push
        config.wizard['hp'] -= g_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.golem['hp'] = config.HP_GOLEM  # Возвращаем здоровье голему после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
            await dp.wait_closed()
            break
        elif config.wizard['hp'] >= 1:  # Действия при победе над големом
            config.golem['hp'] = config.HP_GOLEM
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_GOLEM,
                                   reply_markup=kb.wizard_doors4)
            break


# Действия при атаке 3_2
@dp.callback_query_handler(lambda x: x.data == "wizard_attack3_2")
async def wizard3_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= sp_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            break
        elif config.wizard['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                   reply_markup=kb.wizard_doors4)
            break


# Действия при атаке 4_1
@dp.callback_query_handler(lambda x: x.data == "wizard_attack4_1")
async def wizard4_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= w_push
        config.wizard['hp'] -= sp_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            break
        elif config.wizard['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                   reply_markup=kb.wizard_doors5)
            break


# Действия при атаке 4_2
@dp.callback_query_handler(lambda x: x.data == "wizard_attack4_2")
async def wizard4_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        sk_push = random.randint(1, config.skeleton['pw'])
        config.skeleton['hp'] -= w_push
        config.wizard['hp'] -= sk_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье скелету после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            break
        elif config.wizard['hp'] >= 1:
            config.skeleton['hp'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                   reply_markup=kb.wizard_doors5)
            break


# Действия при атаке 5
@dp.callback_query_handler(lambda x: x.data == "wizard_attack5")
async def wizard5_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.wizard['hp'] > 0 and config.demon['hp'] > 0:
        w_push = random.randint(1, config.wizard['pw'])
        de_push = random.randint(1, config.demon['pw'])
        config.demon['hp'] -= w_push
        config.wizard['hp'] -= de_push
        if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
            config.demon['hp'] = config.HP_DEMON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_DEMON_WIZARD)
            break
        elif config.wizard['hp'] >= 1:
            config.demon['hp'] = config.HP_DEMON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.END_GAME_WIZARD)
            break


'''
Функции побега волшебника
'''


# Действия при побеге 1_1(переход в 1_2(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away1_1")
async def wizard1_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sl_push = random.randint(1, config.slime['pw'])
            config.slime['hp'] -= w_push
            config.wizard['hp'] -= sl_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.wizard_doors2)
                break


# Действия при побеге 1_2(переход в 1_1(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "wizard_away1_2")
async def wizard1_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= sp_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors2)
                break


# Действия при побеге 2_1(переход в 2_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away2_1")
async def wizard2_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 3
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sk_push = random.randint(1, config.skeleton['pw'])
            config.skeleton['hp'] -= w_push
            config.wizard['hp'] -= sk_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.wizard_doors3)
                break


# Действия при побеге 2_2(переход в 2_1(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away2_2")
async def wizard2_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 7
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.slime['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sl_push = random.randint(1, config.slime['pw'])
            config.slime['hp'] -= w_push
            config.wizard['hp'] -= sl_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.wizard_doors3)
                break


# Действия при побеге 3_1(переход в 3_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "wizard_away3_1")
async def wizard3_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_GOLEM)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 9
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= sp_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors4)
                break


# Действия при побеге 3_2(переход в 3_1(битва с големом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away3_2")
async def wizard3_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_GOLEM)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.golem['hp'] > 0:
            w_push = random.randint(1, config.golem['pw'])
            g_push = random.randint(1, config.golem['pw'])
            config.golem['hp'] -= w_push
            config.wizard['hp'] -= g_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.golem['hp'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:  # Действия при победе над големом
                config.golem['hp'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors4)
                break


# Действия при побеге 4_1(переход в 4_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away4_1")
async def wizard4_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 5
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.skeleton['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sk_push = random.randint(1, config.skeleton['pw'])
            config.skeleton['hp'] -= w_push
            config.wizard['hp'] -= sk_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.wizard_doors5)
                break


# Действия при побеге 4_2(переход в 4_1(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "wizard_away4_2")
async def wizard4_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 7
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= sp_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors5)
                break


# РЫЦАРЬ
@dp.callback_query_handler(lambda x: x.data == "knight")
async def knight_delete_button(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.KNIGHT_HISTORY)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.KNIGHT_START_TEXT,
                           reply_markup=kb.knight_doors1)


'''
Функции вывода кнопок рыцаря
'''


# 1_1 Скелет
@dp.callback_query_handler(lambda x: x.data == "knight_door1_1")
async def knight_room1_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.knight_battle1_1)


# 1_2 Паук
@dp.callback_query_handler(lambda x: x.data == "knight_door1_2")
async def knight_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.knight_battle1_2)


# 2_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "knight_door2_1")
async def knight_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.knight_battle2_1)


# 2_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "knight_door2_2")
async def knight_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.knight_battle2_2)


# 3_1 Голем
@dp.callback_query_handler(lambda x: x.data == "knight_door3_1")
async def knight_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.GOLEM_MEETING,
                           reply_markup=kb.knight_battle3_1)


# 3_2 Паук
@dp.callback_query_handler(lambda x: x.data == "knight_door3_2")
async def knight_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.knight_battle3_2)


# 4_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "knight_door4_1")
async def knight_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.knight_battle4_1)


# 4_2 Голем
@dp.callback_query_handler(lambda x: x.data == "knight_door4_2")
async def knight_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.GOLEM_MEETING,
                           reply_markup=kb.knight_battle4_2)


# 5 Дракон
@dp.callback_query_handler(lambda x: x.data == "knight_door5")
async def wizard_room5_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    config.knight['hp'] += 15
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.BONUS_HP + str(config.knight['hp']))
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.DRAGON_MEETING,
                           reply_markup=kb.knight_battle5)


'''
Функции атаки рыцаря
'''


# Действия при атаке 1_1
@dp.callback_query_handler(lambda x: x.data == "knight_attack1_1")
async def knight1_1attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.skeleton['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        sk_push = random.randint(1, config.skeleton['pw'])
        config.skeleton['hp'] -= k_push
        config.knight['hp'] -= sk_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье скелету после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:
            config.skeleton['hp'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                   reply_markup=kb.knight_doors2)
            break


# Действия при атаке 1_2
@dp.callback_query_handler(lambda x: x.data == "knight_attack1_2")
async def knight1_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.spider['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= k_push
        config.knight['hp'] -= sp_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                   reply_markup=kb.knight_doors2)
            break


# Действия при атаке 2_1
@dp.callback_query_handler(lambda x: x.data == "knight_attack2_1")
async def knight2_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.slime['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        sl_push = random.randint(1, config.slime['pw'])
        config.slime['hp'] -= k_push
        config.knight['hp'] -= sl_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье слайму после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:
            config.slime['hp'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                   reply_markup=kb.knight_doors3)
            break


# Действия при атаке 2_2
@dp.callback_query_handler(lambda x: x.data == "knight_attack2_2")
async def knight2_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.skeleton['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        sk_push = random.randint(1, config.skeleton['pw'])
        config.skeleton['hp'] -= k_push
        config.knight['hp'] -= sk_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['hp'] = config.HP_SKELETON  # Возвращаем здоровье скелету после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:
            config.skeleton['hp'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                   reply_markup=kb.knight_doors3)
            break


# Действия при атаке 3_1
@dp.callback_query_handler(lambda x: x.data == "knight_attack3_1")
async def knight3_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.golem['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        g_push = random.randint(1, config.golem['pw'])
        config.golem['hp'] -= k_push
        config.knight['hp'] -= g_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.golem['hp'] = config.HP_GOLEM  # Возвращаем здоровье голему после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:  # Действия при победе над големом
            config.golem['hp'] = config.HP_GOLEM
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_GOLEM,
                                   reply_markup=kb.knight_doors4)
            break


# Действия при атаке 3_2
@dp.callback_query_handler(lambda x: x.data == "knight_attack3_2")
async def knight3_2_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.spider['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        sp_push = random.randint(1, config.spider['pw'])
        config.spider['hp'] -= k_push
        config.knight['hp'] -= sp_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:
            config.spider['hp'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                   reply_markup=kb.knight_doors4)
            break


# Действия при атаке 4_1
@dp.callback_query_handler(lambda x: x.data == "knight_attack4_1")
async def knight4_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.slime['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        sl_push = random.randint(1, config.slime['pw'])
        config.slime['hp'] -= k_push
        config.knight['hp'] -= sl_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.slime['hp'] = config.HP_SLIME  # Возвращаем здоровье слайму после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:
            config.slime['hp'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                   reply_markup=kb.knight_doors5)
            break


# Действия при атаке 4_2
@dp.callback_query_handler(lambda x: x.data == "knight_attack4_2")
async def knight3_1_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.golem['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        g_push = random.randint(1, config.golem['pw'])
        config.golem['hp'] -= k_push
        config.knight['hp'] -= g_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.golem['hp'] = config.HP_GOLEM  # Возвращаем здоровье голему после драки
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['hp'] >= 1:  # Действия при победе над големом
            config.golem['hp'] = config.HP_GOLEM
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
            # Создание кнопок второй комнаты
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_GOLEM,
                                   reply_markup=kb.knight_doors4)
            break


# Действия при атаке 5
@dp.callback_query_handler(lambda x: x.data == "knight_attack5")
async def knight5_attack(callback_query: types.CallbackQuery):
    # Удаление кнопок
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    # Цикл атаки
    while config.knight['hp'] > 0 and config.dragon['hp'] > 0:
        k_push = random.randint(1, config.knight['pw'])
        dr_push = random.randint(1, config.dragon['pw'])
        config.dragon['hp'] -= k_push
        config.knight['hp'] -= dr_push
        if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
            config.dragon['hp'] = config.HP_DRAGON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_DRAGON_WIZARD)
            break
        elif config.knight['hp'] >= 1:
            config.dragon['hp'] = config.HP_DRAGON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.END_GAME_KNIGHT)
            break


'''
Функции побега рыцаря
'''


# Действия при побеге 1_1(переход в 1_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "knight_away1_1")
async def knight1_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.knight['hp'] -= 7
    if config.knight['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(2)
        # Цикл атаки
        while config.knight['hp'] > 0 and config.spider['hp'] > 0:
            k_push = random.randint(1, config.knight['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= k_push
            config.knight['hp'] -= sp_push
            if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.knight_doors2)
                break


# Действия при побеге 1_2(переход в 1_1(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "knight_away1_2")
async def knight_1_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.knight['hp'] -= 5
    if config.knight['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(2)
        # Цикл атаки
        while config.knight['hp'] > 0 and config.skeleton['hp'] > 0:
            k_push = random.randint(1, config.knight['pw'])
            sk_push = random.randint(1, config.skeleton['pw'])
            config.skeleton['hp'] -= k_push
            config.knight['hp'] -= sk_push
            if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['hp'] >= 1:
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.knight_doors2)
                break


# Действия при побеге 2_1(переход в 2_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "knight_away2_1")
async def knight2_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.knight['hp'] -= 3
    if config.knight['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(2)
        # Цикл атаки
        while config.knight['hp'] > 0 and config.skeleton['hp'] > 0:
            k_push = random.randint(1, config.knight['pw'])
            sk_push = random.randint(1, config.skeleton['pw'])
            config.skeleton['hp'] -= k_push
            config.knight['hp'] -= sk_push
            if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['hp'] >= 1:
                config.skeleton['hp'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.knight_doors3)
                break


# Действия при побеге 2_2(переход в 2_1(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "knight_away2_2")
async def knight2_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.knight['hp'] -= 7
    if config.knight['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(2)
        # Цикл атаки
        while config.knight['hp'] > 0 and config.slime['hp'] > 0:
            k_push = random.randint(1, config.knight['pw'])
            sl_push = random.randint(1, config.slime['pw'])
            config.slime['hp'] -= k_push
            config.knight['hp'] -= sl_push
            if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['hp'] >= 1:
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.knight_doors3)
                break


# Действия при побеге 3_1(переход в 3_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "wizard_away3_1")
async def wizard3_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_GOLEM)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.wizard['hp'] -= 9
    if config.wizard['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(2)
        # Цикл атаки
        while config.wizard['hp'] > 0 and config.spider['hp'] > 0:
            w_push = random.randint(1, config.wizard['pw'])
            sp_push = random.randint(1, config.spider['pw'])
            config.spider['hp'] -= w_push
            config.wizard['hp'] -= sp_push
            if config.wizard['hp'] <= 0:  # Проверка жив ли персонаж
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['hp'] >= 1:
                config.spider['hp'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors4)
                break


# Действия при побеге 3_2(переход в 3_1(битва с големом))
@dp.callback_query_handler(lambda x: x.data == "knight_away3_2")
async def knight3_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.knight['hp'] -= 5
    if config.knight['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_GOLEM)
        time.sleep(2)
        # Цикл атаки
        while config.knight['hp'] > 0 and config.golem['hp'] > 0:
            k_push = random.randint(1, config.golem['pw'])
            g_push = random.randint(1, config.golem['pw'])
            config.golem['hp'] -= k_push
            config.knight['hp'] -= g_push
            if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
                config.golem['hp'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['hp'] >= 1:  # Действия при победе над големом
                config.golem['hp'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_GOLEM,
                                       reply_markup=kb.knight_doors4)
                break


# Действия при побеге 4_1(переход в 4_2(битва с големом))
@dp.callback_query_handler(lambda x: x.data == "knight_away4_1")
async def knight4_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.knight['hp'] -= 3
    if config.knight['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_GOLEM)
        time.sleep(2)
        # Цикл атаки
        while config.knight['hp'] > 0 and config.golem['hp'] > 0:
            k_push = random.randint(1, config.golem['pw'])
            g_push = random.randint(1, config.golem['pw'])
            config.golem['hp'] -= k_push
            config.knight['hp'] -= g_push
            if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
                config.golem['hp'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['hp'] >= 1:  # Действия при победе над големом
                config.golem['hp'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_GOLEM,
                                       reply_markup=kb.knight_doors5)
                break


# Действия при побеге 4_2(переход в 4_1(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "knight_away4_2")
async def knight4_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_GOLEM)
    time.sleep(2)
    # Проверка количества здоровья после побега
    config.knight['hp'] -= 9
    if config.knight['hp'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['hp']))
        time.sleep(1)
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(2)
        # Цикл атаки
        while config.knight['hp'] > 0 and config.slime['hp'] > 0:
            k_push = random.randint(1, config.knight['pw'])
            sl_push = random.randint(1, config.slime['pw'])
            config.slime['hp'] -= k_push
            config.knight['hp'] -= sl_push
            if config.knight['hp'] <= 0:  # Проверка жив ли персонаж
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['hp'] >= 1:
                config.slime['hp'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['hp']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.knight_doors5)
                break


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
