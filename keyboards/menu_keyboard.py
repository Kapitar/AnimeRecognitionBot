from aiogram import types

menu_anime_detect_button = "Распознать аниме персонажа"
menu_human_to_anime_button = "На кого ты похож из аниме"

row = [
    types.KeyboardButton(text=menu_anime_detect_button),
    types.KeyboardButton(text=menu_human_to_anime_button),
]


menu_keyboard = types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)