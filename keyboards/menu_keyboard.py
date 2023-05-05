"""Keyboard for main menu"""
from aiogram import types

MENU_ANIME_DETECT_BUTTON = "Распознать аниме персонажа"


row = [
    types.KeyboardButton(text=MENU_ANIME_DETECT_BUTTON),
]


menu_keyboard = types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
