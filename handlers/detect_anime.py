from aiogram import Router, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,  ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State

from PIL import Image

from keyboards.menu_keyboard import menu_button
from keyboards.back_keyboard import back_keyboard
from texts import client_text as texts
from main import bot

MIN_SIZE = 64

router = Router()


class DetectAnime(StatesGroup):
    waiting_for_image = State()


@router.message(Text(menu_button))
async def wait_for_image(message: Message, state: FSMContext):
    await message.answer(texts.WAITING_FOR_IMAGE, reply_markup=back_keyboard)
    await state.set_state(DetectAnime.waiting_for_image)


@router.message(DetectAnime.waiting_for_image, F.photo)
async def image_chosen(message: Message, state: FSMContext):
    photo_size = message.photo[-1]
    if photo_size.width < MIN_SIZE or photo_size.height < MIN_SIZE:
        return await message.answer(texts.BAD_IMAGE_ERROR)

    file = await bot.get_file(photo_size.file_id)
    file_path = file.file_path
    ext = file_path.split(".")[-1]
    await bot.download_file(file_path, f"photos/{message.from_user.id}.{ext}")

    im = Image.open(f"photos/{message.from_user.id}.{ext}")
    out = im.resize((MIN_SIZE, MIN_SIZE))
    out.save(f"photos/{message.from_user.id}.{ext}")

    await message.answer(texts.WAIT_FOR_RENDER, reply_markup=ReplyKeyboardRemove())


@router.message(DetectAnime.waiting_for_image)
async def image_chosen_incorrectly(message: Message, state: FSMContext):
    await message.answer(texts.NOT_IMAGE_ERROR, reply_markup=back_keyboard)