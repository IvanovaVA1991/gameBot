from aiogram import Dispatcher,  types
from create_bot import *
import random

async def command_start(message: types.Message):
    await message.answer('Привет! С этим ботом можно сыграть в игру. Доступные команды: /start, /help \
        - начать общение, получить информацию, /rules - правила игры, /game - начать новую игру')


async def command_rules(message: types.Message):
    await message.answer('На столе лежит 150 конфет. Кто ходит первым, определяется рандомно.\
                        За один ход можно забрать от 1 до 28 конфет. Все конфеты оппонента достаются\
                        сделавшему последний ход.')

n = 150
m = 28


async def command_game(message: types.Message):
    global n
    n = 150
    firstPlayer = random.randint(1, 2)   #1 - user, 2 - bot
    if firstPlayer == 1:
        await message.answer('Ходи первым! Пример сообщения: /беру 15')
    else:
        k = n%(m+1)
        n = n-k
        await message.answer(f'Я хожу первым и беру {k} конфет. Осталось {n} конфет. \
            Твой ход! Пример сообщения: /беру 15') 

async def command_take(message: types.Message):  
    global n
    global m
    msg = message.text
    items = msg.split()
    k = int(items[1])
    if k>m:
        await message.answer('По правилам можно взять от 1 до 28 конфет! Ходи еще раз')
    else:
        n = n-k
        if  m*2+1 >= n > m + 1:
            await message.answer(f'Осталось {n} конфет')
            k = n-m-1
            n = n-k
            await message.answer(f'Я беру {k} конфет, осталось {n}')
        elif n == 0:
            await message.answer('Поздравляю, ты победил!')
            await message.answer('Для новой игры введи команду /game или сделай ход командой /беру. \
                Если хочешь еще раз прочитать правила - команда /rules')
            n = 150
        elif n<=m:
            if k>n+k:
                n += k
                await message.answer(f'Осталось только {n} конфет, больше взять нельзя! Ходи еще раз')
            else:
                await message.answer(f'Осталось {n} конфет')
                await message.answer(f'Я беру {n} конфет и я победил!')
                await message.answer('Для новой игры введи команду /game или сделай ход командой /беру.  \
                    Если хочешь еще раз прочитать правила - команда /rules')
                n = 150
        else:
            await message.answer(f'Осталось {n} конфет')
            k = random.randint(1, 28)
            n = n-k
            await message.answer(f'Я беру {k} конфет, осталось {n}')
                


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_rules, commands=['rules'])
    dp.register_message_handler(command_game, commands=['game'])
    dp.register_message_handler(command_take, commands=['беру'])
