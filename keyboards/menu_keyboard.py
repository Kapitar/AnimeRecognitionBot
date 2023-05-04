from aiogram import types

menu_button = "Распознать аниме персонажа"

menu_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text=menu_button)]], resize_keyboard=True)