from PIL import Image
from utils.constants import MIN_SIZE
from main import bot
from aiogram.types import PhotoSize


async def save_image(photo_size: PhotoSize, user_id: int) -> str:
    file = await bot.get_file(photo_size.file_id)
    file_path = file.file_path
    ext = file_path.split(".")[-1]
    path = f"photos/{user_id}.{ext}"
    await bot.download_file(file_path, path)
    return path


def compress_image(path: str):
    im = Image.open(path)
    out = im.resize((MIN_SIZE, MIN_SIZE))
    out.save(path)
