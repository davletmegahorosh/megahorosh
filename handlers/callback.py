from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import bot, dp

async def quiz_2(call: types.CallbackQuery):
    markup2 = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton('Next', callback_data='button2')
    markup2.add(button2)
    question = 'Центр КР?'
    answers = [
        'Бишкек',
        'Ош',
        'Нью-Йорк',
        'ЮАР'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question = question,
        options = answers,
        is_anonymous = False,
        type = 'quiz',
        correct_option_id=0,
        open_period=10,
        reply_markup=markup2,
    )

async def quiz_3(call: types.CallbackQuery):
    question = 'Где лучшие абриксы'
    answers = [
        'США',
        'Россия',
        'Ураина',
        'Баткен'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question = question,
        options = answers,
        is_anonymous = False,
        type = 'quiz',
        correct_option_id=3,
        open_period=10,
    )

def register_handlers_callback(dp : Dispatcher):
    dp.register_callback_query_handler(quiz_2, text = 'button1')
    dp.register_callback_query_handler(quiz_3, text='button2')