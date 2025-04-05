from datetime import *
import random
import time
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram import executor

import config
import keyboard as kb

name = ''  # Переменная, в которую записывается каждый раз имя игрока взятое из телеграмма
chart_name = ''  # Переменная, в которую будет записываться имя персонажа выбранного игроком
status = ''  # Переменная, в которой хранится информация о победе или поражении игрока
date = datetime.now().strftime("%Y-%m-%d %H:%M")  # Получаем текущую дату и время


def uploading_statistics_in_database(username=name, times=date, win_lose=status, character=chart_name):
    conn = sqlite3.connect(config.db_file)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Rating (username, time, win_lose, character) VALUES (?, ?, ?, ?)",
        (username, times, win_lose, character))
    conn.commit()
    conn.close()


def get_statistic():
    ...  # тут будет запрос, который будет выводить нужную статистику по username


# @Dungeon_GameBot
bot = Bot(token=config.TOKEN_API)
# bot = Bot(token=config.TOKEN_API, proxy='http://10.0.48.52:3128')
dp = Dispatcher(bot=bot)


# ОСНОВНЫЕ КНОПКИ
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=f"Здравствуй {message.from_user.full_name}!" + config.START_TEXT, reply_markup=kb.keyb)




@dp.message_handler(text=['Статистика📋'])
async def information_command(message: types.Message):
    await message.answer(text='ТУТ СКОРО БУДЕТ СТАТИСТИКА!')
    # await message.answer(text=get_statistic(...))


@dp.message_handler(text=['Информацияℹ️'])
async def information_command(message: types.Message):
    await message.answer(text=config.INFORMATION_TEXT)


@dp.message_handler(text=['Начать игру🎮'])
async def start_command(message: types.Message):
    config.wizard['health'] = config.HP_WIZARD
    config.knight['health'] = config.HP_KNIGHT

    media = [
        types.InputMediaPhoto(open(config.wizard_img, 'rb')),
        types.InputMediaPhoto(open(config.knight_img, 'rb'))
    ]
    await bot.send_media_group(chat_id=message.chat.id, media=media)

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
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.wizard_battle1_1)


# 1_2 Слайм

@dp.callback_query_handler(lambda x: x.data == "wizard_door1_2")
async def wizard_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.wizard_battle1_2)


# 2_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "wizard_door2_1")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.wizard_battle2_1)


# 2_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "wizard_door2_2")
async def wizard_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.wizard_battle2_2)


# 3_1 Голем
@dp.callback_query_handler(lambda x: x.data == "wizard_door3_1")
async def wizard_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.golem_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.GOLEM_MEETING,
                           reply_markup=kb.wizard_battle3_1)


# 3_2 Паук
@dp.callback_query_handler(lambda x: x.data == "wizard_door3_2")
async def wizard_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.wizard_battle3_2)


# 4_1 Паук
@dp.callback_query_handler(lambda x: x.data == "wizard_door4_1")
async def wizard_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.wizard_battle4_1)


# 4_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "wizard_door4_2")
async def wizard_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.wizard_battle4_2)


# 5 Демон
@dp.callback_query_handler(lambda x: x.data == "wizard_door5")
async def wizard_room5_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    config.wizard['health'] += 15
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.BONUS_HP + str(config.wizard['health']))
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.demon_img, 'rb'))])
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
    while config.wizard['health'] > 0 and config.spider['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        sp_push = random.randint(1, config.spider['power'])
        config.spider['health'] -= w_push
        config.wizard['health'] -= sp_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.spider['health'] = config.HP_SPIDER
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            break
        elif config.wizard['health'] >= 1:
            config.spider['health'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.slime['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        sl_push = random.randint(1, config.slime['power'])
        config.slime['health'] -= w_push
        config.wizard['health'] -= sl_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.slime['health'] = config.HP_SLIME  # Возвращаем здоровье слайму
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            await dp.wait_closed()
            break
        elif config.wizard['health'] >= 1:
            config.slime['health'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)

            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.slime['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        sl_push = random.randint(1, config.slime['power'])
        config.slime['health'] -= w_push
        config.wizard['health'] -= sl_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.slime['health'] = config.HP_SLIME  # Возвращаем здоровье слайму
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            await dp.wait_closed()
            break
        elif config.wizard['health'] >= 1:
            config.slime['health'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.skeleton['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        sk_push = random.randint(1, config.skeleton['power'])
        config.skeleton['health'] -= w_push
        config.wizard['health'] -= sk_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['health'] = config.HP_SKELETON  # Возвращаем здоровье скелету
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            await dp.wait_closed()
            break
        elif config.wizard['health'] >= 1:
            config.skeleton['health'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.golem['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        g_push = random.randint(1, config.golem['power'])
        config.golem['health'] -= w_push
        config.wizard['health'] -= g_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.golem['health'] = config.HP_GOLEM  # Возвращаем здоровье голему
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
            await dp.wait_closed()
            break
        elif config.wizard['health'] >= 1:  # Действия при победе над големом
            config.golem['health'] = config.HP_GOLEM
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.spider['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        sp_push = random.randint(1, config.spider['power'])
        config.spider['health'] -= w_push
        config.wizard['health'] -= sp_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.spider['health'] = config.HP_SPIDER
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            break
        elif config.wizard['health'] >= 1:
            config.spider['health'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.spider['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        sp_push = random.randint(1, config.spider['power'])
        config.spider['health'] -= w_push
        config.wizard['health'] -= sp_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.spider['health'] = config.HP_SPIDER
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            break
        elif config.wizard['health'] >= 1:
            config.spider['health'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.skeleton['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        sk_push = random.randint(1, config.skeleton['power'])
        config.skeleton['health'] -= w_push
        config.wizard['health'] -= sk_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['health'] = config.HP_SKELETON  # Возвращаем здоровье скелету
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            break
        elif config.wizard['health'] >= 1:
            config.skeleton['health'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            await dp.wait_closed()
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    while config.wizard['health'] > 0 and config.demon['health'] > 0:
        w_push = random.randint(1, config.wizard['power'])
        de_push = random.randint(1, config.demon['power'])
        config.demon['health'] -= w_push
        config.wizard['health'] -= de_push
        if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
            config.demon['health'] = config.HP_DEMON
            uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_DEMON_WIZARD)
            break
        elif config.wizard['health'] >= 1:
            config.demon['health'] = config.HP_DEMON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.END_GAME_WIZARD)
            uploading_statistics_in_database(win_lose='Победа', character='Wizard')
            break


'''
Функции побега волшебника
'''


# Действия при побеге 1_1(переход в 1_2(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away1_1")
async def wizard1_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_SPIDER
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.slime['health'] > 0:
            w_push = random.randint(1, config.wizard['power'])
            sl_push = random.randint(1, config.slime['power'])
            config.slime['health'] -= w_push
            config.wizard['health'] -= sl_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.slime['health'] = config.HP_SLIME
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:
                config.slime['health'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.wizard_doors2)
                break


# Действия при побеге 1_2(переход в 1_1(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "wizard_away1_2")
async def wizard1_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_SPIDER
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.spider['health'] > 0:
            w_push = random.randint(1, config.wizard['power'])
            sp_push = random.randint(1, config.spider['power'])
            config.spider['health'] -= w_push
            config.wizard['health'] -= sp_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.spider['health'] = config.HP_SPIDER
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:
                config.spider['health'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors2)
                break


# Действия при побеге 2_1(переход в 2_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away2_1")
async def wizard2_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_SLIME
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.skeleton['health'] > 0:
            w_push = random.randint(1, config.wizard['power'])
            sk_push = random.randint(1, config.skeleton['power'])
            config.skeleton['health'] -= w_push
            config.wizard['health'] -= sk_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['health'] = config.HP_SKELETON
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:
                config.skeleton['health'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.wizard_doors3)
                break


# Действия при побеге 2_2(переход в 2_1(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away2_2")
async def wizard2_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_SKELETON
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.slime['health'] > 0:
            w_push = random.randint(1, config.wizard['power'])
            sl_push = random.randint(1, config.slime['power'])
            config.slime['health'] -= w_push
            config.wizard['health'] -= sl_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.slime['health'] = config.HP_SLIME
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:
                config.slime['health'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.wizard_doors3)
                break


# Действия при побеге 3_1(переход в 3_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "wizard_away3_1")
async def wizard3_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_GOLEM)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_GOLEM
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.spider['health'] > 0:
            w_push = random.randint(1, config.wizard['power'])
            sp_push = random.randint(1, config.spider['power'])
            config.spider['health'] -= w_push
            config.wizard['health'] -= sp_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.spider['health'] = config.HP_SPIDER
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:
                config.spider['health'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors4)
                break


# Действия при побеге 3_2(переход в 3_1(битва с големом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away3_2")
async def wizard3_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_SPIDER
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.golem_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_GOLEM)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.golem['health'] > 0:
            w_push = random.randint(1, config.golem['power'])
            g_push = random.randint(1, config.golem['power'])
            config.golem['health'] -= w_push
            config.wizard['health'] -= g_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.golem['health'] = config.HP_GOLEM
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:  # Действия при победе над големом
                config.golem['health'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.wizard_doors4)
                break


# Действия при побеге 4_1(переход в 4_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "wizard_away4_1")
async def wizard4_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_SPIDER
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.skeleton['health'] > 0:
            w_push = random.randint(1, config.wizard['power'])
            sk_push = random.randint(1, config.skeleton['power'])
            config.skeleton['health'] -= w_push
            config.wizard['health'] -= sk_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['health'] = config.HP_SKELETON
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:
                config.skeleton['health'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.wizard_doors5)
                break


# Действия при побеге 4_2(переход в 4_1(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "wizard_away4_2")
async def wizard4_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.wizard['health'] -= config.ESCAPE_PENALTY_SKELETON
    if config.wizard['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.wizard['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(1)
        # Цикл атаки
        while config.wizard['health'] > 0 and config.spider['health'] > 0:
            w_push = random.randint(1, config.wizard['power'])
            sp_push = random.randint(1, config.spider['power'])
            config.spider['health'] -= w_push
            config.wizard['health'] -= sp_push
            if config.wizard['health'] <= 0:  # Проверка жив ли персонаж
                config.spider['health'] = config.HP_SPIDER
                uploading_statistics_in_database(win_lose='Поражение', character='Wizard')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.wizard['health'] >= 1:
                config.spider['health'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.wizard['health']))
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
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.knight_battle1_1)


# 1_2 Паук
@dp.callback_query_handler(lambda x: x.data == "knight_door1_2")
async def knight_room1_buttons(callback_query: types.CallbackQuery):  # Функция с основным выводом текста
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.knight_battle1_2)


# 2_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "knight_door2_1")
async def knight_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.knight_battle2_1)


# 2_2 Скелет
@dp.callback_query_handler(lambda x: x.data == "knight_door2_2")
async def knight_room2_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SKELETON_MEETING,
                           reply_markup=kb.knight_battle2_2)


# 3_1 Голем
@dp.callback_query_handler(lambda x: x.data == "knight_door3_1")
async def knight_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.golem_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.GOLEM_MEETING,
                           reply_markup=kb.knight_battle3_1)


# 3_2 Паук
@dp.callback_query_handler(lambda x: x.data == "knight_door3_2")
async def knight_room3_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SPIDER_MEETING,
                           reply_markup=kb.knight_battle3_2)


# 4_1 Слайм
@dp.callback_query_handler(lambda x: x.data == "knight_door4_1")
async def knight_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.SLIME_MEETING,
                           reply_markup=kb.knight_battle4_1)


# 4_2 Голем
@dp.callback_query_handler(lambda x: x.data == "knight_door4_2")
async def knight_room4_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.golem_img, 'rb'))])
    # вывод кнопок
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.GOLEM_MEETING,
                           reply_markup=kb.knight_battle4_2)


# 5 Дракон
@dp.callback_query_handler(lambda x: x.data == "knight_door5")
async def wizard_room5_delete_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    config.knight['health'] += 15
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.BONUS_HP + str(config.knight['health']))
    await bot.send_media_group(chat_id=callback_query.from_user.id,
                               media=[types.InputMediaPhoto(open(config.dragon_img, 'rb'))])
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
    while config.knight['health'] > 0 and config.skeleton['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        sk_push = random.randint(1, config.skeleton['power'])
        config.skeleton['health'] -= k_push
        config.knight['health'] -= sk_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['health'] = config.HP_SKELETON  # Возвращаем здоровье скелету 
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:
            config.skeleton['health'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.spider['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        sp_push = random.randint(1, config.spider['power'])
        config.spider['health'] -= k_push
        config.knight['health'] -= sp_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.spider['health'] = config.HP_SPIDER
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:
            config.spider['health'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.slime['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        sl_push = random.randint(1, config.slime['power'])
        config.slime['health'] -= k_push
        config.knight['health'] -= sl_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.slime['health'] = config.HP_SLIME  # Возвращаем здоровье слайму
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:
            config.slime['health'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.skeleton['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        sk_push = random.randint(1, config.skeleton['power'])
        config.skeleton['health'] -= k_push
        config.knight['health'] -= sk_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.skeleton['health'] = config.HP_SKELETON  # Возвращаем здоровье скелету
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:
            config.skeleton['health'] = config.HP_SKELETON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.golem['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        g_push = random.randint(1, config.golem['power'])
        config.golem['health'] -= k_push
        config.knight['health'] -= g_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.golem['health'] = config.HP_GOLEM  # Возвращаем здоровье голему
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:  # Действия при победе над големом
            config.golem['health'] = config.HP_GOLEM
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.spider['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        sp_push = random.randint(1, config.spider['power'])
        config.spider['health'] -= k_push
        config.knight['health'] -= sp_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.spider['health'] = config.HP_SPIDER
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:
            config.spider['health'] = config.HP_SPIDER
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.slime['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        sl_push = random.randint(1, config.slime['power'])
        config.slime['health'] -= k_push
        config.knight['health'] -= sl_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.slime['health'] = config.HP_SLIME  # Возвращаем здоровье слайму
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:
            config.slime['health'] = config.HP_SLIME
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.golem['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        g_push = random.randint(1, config.golem['power'])
        config.golem['health'] -= k_push
        config.knight['health'] -= g_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.golem['health'] = config.HP_GOLEM  # Возвращаем здоровье голему
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
            dp.stop_polling()
            await dp.wait_closed()
            await bot.close()
            break
        elif config.knight['health'] >= 1:  # Действия при победе над големом
            config.golem['health'] = config.HP_GOLEM
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
            # Вывод здоровья
            await bot.send_message(chat_id=callback_query.from_user.id,
                                   text=config.AFTER_FIGHT_HP + str(config.knight['health']))
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
    while config.knight['health'] > 0 and config.dragon['health'] > 0:
        k_push = random.randint(1, config.knight['power'])
        dr_push = random.randint(1, config.dragon['power'])
        config.dragon['health'] -= k_push
        config.knight['health'] -= dr_push
        if config.knight['health'] <= 0:  # Проверка жив ли персонаж
            config.dragon['health'] = config.HP_DRAGON
            uploading_statistics_in_database(win_lose='Поражение', character='Knight')
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_DRAGON_WIZARD)
            break
        elif config.knight['health'] >= 1:
            config.dragon['health'] = config.HP_DRAGON
            await bot.send_message(chat_id=callback_query.from_user.id, text=config.END_GAME_KNIGHT)
            uploading_statistics_in_database(win_lose='Победа', character='Knight')
            break


'''
Функции побега рыцаря
'''


# Действия при побеге 1_1(переход в 1_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "knight_away1_1")
async def knight1_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_SKELETON
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.spider['health'] > 0:
            k_push = random.randint(1, config.knight['power'])
            sp_push = random.randint(1, config.spider['power'])
            config.spider['health'] -= k_push
            config.knight['health'] -= sp_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.spider['health'] = config.HP_SPIDER
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:
                config.spider['health'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.knight_doors2)
                break


# Действия при побеге 1_2(переход в 1_1(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "knight_away1_2")
async def knight_1_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_SPIDER
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.skeleton['health'] > 0:
            k_push = random.randint(1, config.knight['power'])
            sk_push = random.randint(1, config.skeleton['power'])
            config.skeleton['health'] -= k_push
            config.knight['health'] -= sk_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['health'] = config.HP_SKELETON
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:
                config.skeleton['health'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.knight_doors2)
                break


# Действия при побеге 2_1(переход в 2_2(битва со скелетом))
@dp.callback_query_handler(lambda x: x.data == "knight_away2_1")
async def knight2_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_SLIME
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.skeleton_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SKELETON)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.skeleton['health'] > 0:
            k_push = random.randint(1, config.knight['power'])
            sk_push = random.randint(1, config.skeleton['power'])
            config.skeleton['health'] -= k_push
            config.knight['health'] -= sk_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.skeleton['health'] = config.HP_SKELETON
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SKELETON)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:
                config.skeleton['health'] = config.HP_SKELETON
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SKELETON)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SKELETON,
                                       reply_markup=kb.knight_doors3)
                break


# Действия при побеге 2_2(переход в 2_1(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "knight_away2_2")
async def knight2_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SKELETON)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_SKELETON
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.slime['health'] > 0:
            k_push = random.randint(1, config.knight['power'])
            sl_push = random.randint(1, config.slime['power'])
            config.slime['health'] -= k_push
            config.knight['health'] -= sl_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.slime['health'] = config.HP_SLIME
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:
                config.slime['health'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.knight_doors3)
                break


# Действия при побеге 3_1(переход в 3_2(битва с пауком))
@dp.callback_query_handler(lambda x: x.data == "knight_away3_1")
async def knight3_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_GOLEM)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_GOLEM
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.spider_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SPIDER)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.spider['health'] > 0:
            k_push = random.randint(1, config.knight['power'])
            sp_push = random.randint(1, config.spider['power'])
            config.spider['health'] -= k_push
            config.knight['health'] -= sp_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.spider['health'] = config.HP_SPIDER
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SPIDER)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:
                config.spider['health'] = config.HP_SPIDER
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SPIDER)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SPIDER,
                                       reply_markup=kb.knight_doors4)
                break


# Действия при побеге 3_2(переход в 3_1(битва с големом))
@dp.callback_query_handler(lambda x: x.data == "knight_away3_2")
async def knight3_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SPIDER)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_SPIDER
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.golem_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_GOLEM)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.golem['health'] > 0:
            k_push = random.randint(1, config.golem['power'])
            g_push = random.randint(1, config.golem['power'])
            config.golem['health'] -= k_push
            config.knight['health'] -= g_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.golem['health'] = config.HP_GOLEM
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:  # Действия при победе над големом
                config.golem['health'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_GOLEM,
                                       reply_markup=kb.knight_doors4)
                break


# Действия при побеге 4_1(переход в 4_2(битва с големом))
@dp.callback_query_handler(lambda x: x.data == "knight_away4_1")
async def knight4_1_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_SLIME)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_SLIME
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.golem_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_GOLEM)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.golem['health'] > 0:
            k_push = random.randint(1, config.golem['power'])
            g_push = random.randint(1, config.golem['power'])
            config.golem['health'] -= k_push
            config.knight['health'] -= g_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.golem['health'] = config.HP_GOLEM
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_GOLEM)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:  # Действия при победе над големом
                config.golem['health'] = config.HP_GOLEM
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_GOLEM)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_GOLEM,
                                       reply_markup=kb.knight_doors5)
                break


# Действия при побеге 4_2(переход в 4_1(битва со слаймом))
@dp.callback_query_handler(lambda x: x.data == "knight_away4_2")
async def knight4_2_away(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id, None, None)
    await bot.send_message(chat_id=callback_query.from_user.id, text=config.AWAY_TEXT_GOLEM)
    time.sleep(1)
    # Проверка количества здоровья после побега
    config.knight['health'] -= config.ESCAPE_PENALTY_GOLEM
    if config.knight['health'] <= 0:  # если нет здоровья - конец
        await bot.send_message(callback_query.from_user.id, text=config.NO_HP_DEAD)
        uploading_statistics_in_database(win_lose='Поражение', character='Knight')
    else:  # если здоровье есть
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=config.AFTER_AWAY + str(config.knight['health']))
        time.sleep(1)
        await bot.send_media_group(chat_id=callback_query.from_user.id,
                                   media=[types.InputMediaPhoto(open(config.slime_img, 'rb'))])
        await bot.send_message(chat_id=callback_query.from_user.id, text=config.TRANSITION_SLIME)
        time.sleep(1)
        # Цикл атаки
        while config.knight['health'] > 0 and config.slime['health'] > 0:
            k_push = random.randint(1, config.knight['power'])
            sl_push = random.randint(1, config.slime['power'])
            config.slime['health'] -= k_push
            config.knight['health'] -= sl_push
            if config.knight['health'] <= 0:  # Проверка жив ли персонаж
                config.slime['health'] = config.HP_SLIME
                uploading_statistics_in_database(win_lose='Поражение', character='Knight')
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_DEAD_SLIME)
                dp.stop_polling()
                await dp.wait_closed()
                await bot.close()
                break
            elif config.knight['health'] >= 1:
                config.slime['health'] = config.HP_SLIME
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.YOU_WIN_SLIME)
                # Вывод здоровья
                await bot.send_message(chat_id=callback_query.from_user.id,
                                       text=config.AFTER_FIGHT_HP + str(config.knight['health']))
                time.sleep(1)
                await bot.send_message(chat_id=callback_query.from_user.id, text=config.ROOM_SLIME,
                                       reply_markup=kb.knight_doors5)
                break


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
