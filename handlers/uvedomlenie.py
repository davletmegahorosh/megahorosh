import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Хорощо наопмню")


async def homework():
    await bot.send_message(chat_id=chat_id, text="Надо начать делать ДЗ!")

async def scheduler():
    aioschedule.every().monday.at("18:00").do(homework)
    aioschedule.every().thursday.at("18:00").do(homework)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'Дз' in word.text)