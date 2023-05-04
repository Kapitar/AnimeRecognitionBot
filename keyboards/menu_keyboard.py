"""Keyboard for main menu"""
from aiogram import types

MENU_ANIME_DETECT_BUTTON = "Распознать аниме персонажа"
MENU_HUMAN_TO_ANIME_BUTTON = "На кого ты похож из аниме"


row = [
    types.KeyboardButton(text=MENU_ANIME_DETECT_BUTTON),
    types.KeyboardButton(text=MENU_HUMAN_TO_ANIME_BUTTON),
]


menu_keyboard = types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
