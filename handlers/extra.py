from aiogram import types, Dispatcher
from config import bot, dp

async def echo(message:types.Message):
    if message.chat.type != 'private':
        bad_words = ['лох']
        username = f'@{message.from_user.username}' if message.from_user.username is not None else message.from_user.full_name
        for i in bad_words:
            if i in message.text:
                await bot.delete_message(message.chat.id, message.message_id)
                await message.answer(f'не матерись {username}, сам ты {i}!')

def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(echo)