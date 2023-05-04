from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.menu_keyboard import menu_keyboard
from keyboards.back_keyboard import back_button
from texts import client_text as texts

router = Router()


@router.message(Command(commands=["start"]))
@router.message(Text(back_button))
async def register(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(texts.WELCOME_TEXT, reply_markup=menu_keyboard)
