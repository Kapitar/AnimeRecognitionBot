from aiogram import types

back_button = "Вернуться на главную"

back_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text=back_button)]], resize_keyboard=True)