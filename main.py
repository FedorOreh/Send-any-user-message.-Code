import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import app.keyboards as kb
bot = Bot(token='your_token')
dp = Dispatcher()


class people1(StatesGroup):
    user_id = State()
    texttwo = State()


@dp.message(Command('people'))
async def people(message: Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    if message.chat.type == 'private':
        if message.from_user.id == 'your id':
            await state.set_state(people1.user_id)
            await bot.send_message(message.from_user.id, '<b><u>Please send user_id</u></b>',
                                   reply_markup=kb.cancel_people, parse_mode='html')
        else:
            await bot.send_message(message.from_user.id, '<b><u>You cannot do this!</u></b>',
                                   parse_mode='html')


@dp.message(people1.user_id)
async def user_idi(message: Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await state.update_data(user_id=message.text)
    await bot.send_message(message.from_user.id, '<b><u>Please send text!</u></b>',
                           reply_markup=kb.cancel_people, parse_mode='html')
    await state.set_state(people1.texttwo)


@dp.callback_query(F.data == 'cancelpeople')
async def cancelpeople(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    callback.answer('Cancel')
    return True


@dp.message(people1.texttwo)
async def textok(message: Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await state.update_data(texttwo=message.text)
    data = await state.get_data()
    await bot.send_message(message.from_user.id, f'<b><u>You really want to send message to this user?\nUser ID: {data["user_id"]}\nText: {data["texttwo"]}</u></b>', 
                     reply_markup=kb.user_confirm, parse_mode='html')
    

@dp.callback_query(F.data == 'confirm_user')
async def confirm_user(message: Message, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(chat_id=data["user_id"], text=data["texttwo"])
    await bot.send_message(message.from_user.id, '<b><u>Message successfully is sended!</u></b>', parse_mode='html')
    await state.clear()


@dp.callback_query(F.data == 'cancel_user')
async def cancel_user(message: Message, state: FSMContext):
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')