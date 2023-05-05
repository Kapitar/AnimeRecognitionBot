"""Keyboard for back actions"""
from aiogram import types

BACK_BUTTON = "Вернуться на главную"

row = [types.KeyboardButton(text=BACK_BUTTON)]
back_keyboard = types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
