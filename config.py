TOKEN_API = "6598630985:AAH6hm8idDR8J4SxkhljfEzBoYnKE4Q4X4s"
# tg: @Dungeon_GameBot

db_file = 'Dungeon_Game.sqlite'

# Пути к изображениям персонажей и монстров
wizard_img = 'image/wizard.png'
knight_img = 'image/knight.png'

spider_img = 'image/spider.png'
slime_img = 'image/slime.png'
golem_img = 'image/golem.png'
skeleton_img = 'image/skeleton.png'

dragon_img = 'image/dragon.png'
demon_img = 'image/demon.png'

# Характеристика персонажей
wizard = dict(name='Волшебник', power=60, health=60)
knight = dict(name='Рыцарь', power=50, health=70)

# Характеристики монстров
slime = dict(name='Слайм', power=15, health=25)
spider = dict(name='Паук', power=20, health=35)
skeleton = dict(name='Скелет', power=25, health=45)
golem = dict(name='Голем', power=30, health=50)

# Характеристики боссов
demon = dict(name='Демон', power=40, health=100)  # Босс для Волшебника
dragon = dict(name='Дракон', power=35, health=100)  # Босс для Рыцаря

# Количество здоровья, которое будет сниматься за побег от определенных монстров
ESCAPE_PENALTY_SLIME = 3
ESCAPE_PENALTY_SPIDER = 4
ESCAPE_PENALTY_SKELETON = 5
ESCAPE_PENALTY_GOLEM = 6

# Здоровье персонажей
HP_KNIGHT = 70
HP_WIZARD = 60

# Здоровье монстров
HP_SLIME = 25
HP_SPIDER = 35
HP_SKELETON = 45
HP_GOLEM = 50

# Здоровье боссов
HP_DEMON = 100
HP_DRAGON = 100

# Текст при запуске бота
START_TEXT = ''' 
Приветствую тебя в моей игре. 
Желаю тебе удачи пройти её!
'''

START_GAME_TEXT = f'''
Перед началом ознакомьтесь с характеристиками персонажей, которых вам надо будет выбрать для прохождения игры:

Характеристики волшебника:
Здоровье: {wizard["health"]}
Сила: {wizard["power"]}

Характеристики рыцаря:
Здоровье: {knight["health"]}
Сила: {knight["power"]}
'''

WIZARD_HISTORY = '''
Волшебник, хороший выбор!
'''

KNIGHT_HISTORY = '''
Рыцарь, хороший выбор!
'''

WIZARD_START_TEXT = '''
Вы появляйтесь в подземелье и видите перед собой две двери, в какую войдете?
'''

KNIGHT_START_TEXT = '''
Вы появляйтесь в подземелье и видите перед собой две двери, в какую войдете?
'''

# Текста при встречах с монстрами
SLIME_MEETING = f'''
Вы встречайте перед собой слайма. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики слайма:
Здоровье: {slime["health"]}
Сила: {slime["power"]}
'''

SPIDER_MEETING = f'''
Вы встречайте перед собой паука. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики паука:
Здоровье: {spider["health"]}
Сила: {spider["power"]}
'''

SKELETON_MEETING = f'''
Вы встречайте перед собой скелета. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики скелета:
Здоровье: {skeleton["health"]}
Сила: {skeleton["power"]}
'''

GOLEM_MEETING = f'''
Вы встречайте перед собой голем. Перед тем как выбрать действие посмотрите характеристики монстра:\n
Характеристики голема:
Здоровье: {golem["health"]}
Сила: {golem["power"]}
'''

DEMON_MEETING = f'''
Входя в огромную комнату, вы встречайте перед собой демона, вот его характеристики:\n
Характеристики демона:
Здоровье: {demon["health"]}
Сила: {demon["power"]}
'''

DRAGON_MEETING = f'''
Входя в огромную комнату, вы встречайте перед собой дракона, вот его характеристики:\n
Характеристики дракона:
Здоровье: {dragon["health"]}
Сила: {dragon["power"]}
'''

YOU_DEAD_DEMON_WIZARD = '''
Вас убил демон!
Игра окончена!
'''

YOU_DEAD_DRAGON_WIZARD = '''
Вас убил дракон!
Игра окончена!
'''

YOU_DEAD_SPIDER = '''
Вы умерли от лап паука!
Игра окончена!
'''

YOU_DEAD_SLIME = '''
Вы умерли от слайма!
Игра окончена!
'''

YOU_DEAD_SKELETON = '''
Вы умерли от скелета!
Игра окончена!
'''

YOU_WIN_SPIDER = '''
Вы победили паука!
'''

AFTER_FIGHT_HP = '''
После боя у вас осталось здоровья: 
'''

AWAY_TEXT_SPIDER = '''
Вы решайте сбежать от паука.\n 
При попытке побега паук вас задевает
и вы теряйте 5 здоровья.
'''

AWAY_TEXT_SLIME = '''
Вы решайте сбежать от слайма.\n 
При попытке побега слайм вас задевает
и вы теряйте 3 здоровья.
'''

AWAY_TEXT_GOLEM = '''
Вы решайте сбежать от голема.\n 
При попытке побега голем вас задевает
и вы теряйте 9 здоровья.
'''

ROOM_SPIDER = '''
После победы над пауком вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

ROOM_SKELETON = '''
После победы над скелетом вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

ROOM_SLIME = '''
После победы над слаймом вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

ROOM_GOLEM = '''
После победы над големом вы проходите в следующую комнату и видите две двери, в какую войдете?
'''

AWAY_TEXT_SKELETON = '''
Вы решайте сбежать от скелета.\n 
При попытке побега он вас задевает
и вы теряйте 7 здоровья.
'''

NO_HP_DEAD = '''
Вы погибли от нехватки здоровья!
Игра окончена!
'''

AFTER_AWAY = '''
После побега у вас осталось здоровья: 
'''

YOU_WIN_SLIME = '''
Вы победили слайма!
'''

YOU_DEAD_GOLEM = '''
Вы умерли от голема!
Игра окончена!
'''

YOU_WIN_GOLEM = '''
Вы победили голема!
'''

YOU_WIN_SKELETON = '''
Вы победили скелета!
'''

TRANSITION_SPIDER = f'''
Войдя в другую дверь, вы видите перед собой паука с характеристиками:\n
Характеристики паука:
Здоровье: {spider["health"]}
Сила: {spider["power"]}\n
Вариантов у вас не будет, вы точно будете сражаться с пауком, т.к сбежали из другой комнаты.
'''

TRANSITION_SLIME = f'''
Войдя в другую дверь, вы видите перед собой слайма с характеристиками:\n
Характеристики слайма:
Здоровье: {slime["health"]}
Сила: {slime["power"]}\n
Вариантов у вас не будет, вы точно будете сражаться со слаймом, т.к сбежали из другой комнаты.
'''

TRANSITION_SKELETON = f'''
Войдя в другую дверь, вы видите перед собой скелета с характеристиками:\n
Характеристики скелета:
Здоровье: {skeleton["health"]}
Сила: {skeleton["power"]}\n
Вариантов у вас не будет, вы точно будете сражаться с скелетом, т.к сбежали из другой комнаты.
'''

TRANSITION_GOLEM = f'''
Войдя в другую дверь, вы видите перед собой голема с характеристиками:\n
Характеристики голема:
Здоровье: {golem["health"]}
Сила: {golem["power"]}\n
Вариантов у вас не будет, вы точно будете сражаться с големом, т.к сбежали из другой комнаты.
'''

AWAY_TEXT_WIZARD = '''
Вы решайте сбежать от голема.\n 
При попытке побега он вас задевает
и вы теряйте 9 здоровья.
'''

END_GAME_WIZARD = '''
Поздравляю, вы победили демона!
Игра пройдена!
'''

END_GAME_KNIGHT = '''
Поздравляю, вы победили дракона!
Игра пройдена!
'''

BONUS_HP = '''
Перед тем, как сразиться с боссом, вы находите бонус +15 здоровья.
Теперь у вас здоровья: 
'''
