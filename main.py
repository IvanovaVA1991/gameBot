from aiogram import executor  #types - типы для написания типов в функциях
import commands
from create_bot import dp
# from aiogram.dispatcher import dispather  #бот ловит события в чате и прописывается реакция
# from aiogram.utils import executor  # чтобы бот вышел в онлайн


# @dp.message_handler(commands=['hi', 'help', 'play'])  # начало взаимодействия с ботом
async def on_startup(_):
    print('Бот вышел в онлайн')
commands.register_handlers_commands(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  #запуск бота, пропускается обновление, чтобы бот не засорялся сообщениями когда не в онлайне
