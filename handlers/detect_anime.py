from aiogram import Router, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,  ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State

from keyboards.menu_keyboard import menu_anime_detect_button, menu_human_to_anime_button
from keyboards.back_keyboard import back_keyboard
from texts import client_text as texts
import utils.images as images
from utils.constants import MIN_SIZE

router = Router()


class DetectAnime(StatesGroup):
    waiting_for_image = State()


@router.message(Text(menu_anime_detect_button))
@router.message(Text(menu_human_to_anime_button))
async def wait_for_image(message: Message, state: FSMContext):
    await message.answer(texts.WAITING_FOR_IMAGE, reply_markup=back_keyboard)
    await state.set_state(DetectAnime.waiting_for_image)
    await state.update_data(mode_type=message.text)


@router.message(DetectAnime.waiting_for_image, F.photo)
async def image_chosen(message: Message, state: FSMContext):
    photo_size = message.photo[-1]
    if photo_size.width < MIN_SIZE or photo_size.height < MIN_SIZE:
        return await message.answer(texts.BAD_IMAGE_ERROR)

    path = await images.save_image(photo_size, message.from_user.id)
    images.compress_image(path)

    await message.answer(texts.WAIT_FOR_RENDER, reply_markup=ReplyKeyboardRemove())
    user_data = await state.get_data()
    if user_data['mode_type'] == menu_anime_detect_button:
        pass
    else:
        pass


@router.message(DetectAnime.waiting_for_image)
async def image_chosen_incorrectly(message: Message):
    await message.answer(texts.NOT_IMAGE_ERROR, reply_markup=back_keyboard)
