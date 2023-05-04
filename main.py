import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import common, detect_anime

import os
from dotenv import load_dotenv
load_dotenv()
bot = Bot(token=os.getenv("TG_TOKEN"))


async def main():
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(common.router)
    dp.include_router(detect_anime.router)

    logging.info("Бот запущен!")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
