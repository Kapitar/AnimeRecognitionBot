"""Work helper for images"""
import torch
from aiogram.types import PhotoSize
from torchvision import transforms
from PIL import Image
from utils.constants import MIN_SIZE
from main import bot

transform_to_tensor = transforms.Compose([
    transforms.ToTensor()
])


async def save_image(photo_size: PhotoSize, user_id: int) -> str:
    """Save image to /photos/"""
    file = await bot.get_file(photo_size.file_id)
    file_path = file.file_path
    ext = file_path.split(".")[-1]
    path = f"photos/{user_id}.{ext}"
    await bot.download_file(file_path, path)
    return path


def compress_image(path: str) -> torch.Tensor:
    """Compress image to MIN_SIZE x MIN_SIZE and returns a tensor"""
    image = Image.open(path)
    out = image.resize((MIN_SIZE, MIN_SIZE))

    x = transform_to_tensor(out)
    x = torch.unsqueeze(x, 0)
    return x
