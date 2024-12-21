from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import types
from aiogram.types import Message

user_confirm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Confirm', callback_data='confirm_user'), InlineKeyboardButton(text='Cancel', callback_data='cancel_user')]
])

cancel_people = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Cancel', callback_data='cancelpeople')]
])