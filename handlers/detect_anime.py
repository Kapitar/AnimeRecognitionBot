"""Provides detect-categoried commands"""
from aiogram import Router, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State

import torch
import torch.nn as nn

from keyboards.menu_keyboard import MENU_ANIME_DETECT_BUTTON
from keyboards.back_keyboard import back_keyboard
from keyboards.menu_keyboard import menu_keyboard
from texts import client_text as texts
from utils import images
from utils.constants import MIN_SIZE
from model.model import get_anime

router = Router()


class DetectAnime(StatesGroup):
    """FSM for anime detection scene"""
    waiting_for_image = State()


@router.message(Text(MENU_ANIME_DETECT_BUTTON))
async def wait_for_image(message: Message, state: FSMContext):
    """Setting a state for waiting for image"""
    await message.answer(texts.WAITING_FOR_IMAGE, reply_markup=back_keyboard)
    await state.set_state(DetectAnime.waiting_for_image)
    await state.update_data(mode_type=message.text)


@router.message(DetectAnime.waiting_for_image, F.photo)
async def image_chosen(message: Message, state: FSMContext):
    """Render an image"""
    photo_size = message.photo[-1]
    if photo_size.width < MIN_SIZE or photo_size.height < MIN_SIZE:
        return await message.answer(texts.BAD_IMAGE_ERROR)

    await message.answer(texts.WAIT_FOR_RENDER, reply_markup=ReplyKeyboardRemove())
    path = await images.save_image(photo_size, message.from_user.id)
    tensor = images.compress_image(path)

    animes = get_anime(tensor)
    answer = texts.GUESS_ANIME + "\n"
    iter = 1
    for chance, name in animes:
        answer += f'{iter}) {name} - {chance}%\n'
        iter += 1

    await message.answer(answer, reply_markup=menu_keyboard)


@router.message(DetectAnime.waiting_for_image)
async def image_chosen_incorrectly(message: Message):
    """Raise an error if the message is not an image"""
    await message.answer(texts.NOT_IMAGE_ERROR, reply_markup=back_keyboard)
