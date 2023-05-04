"""Main running file"""
import os
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import common, detect_anime

load_dotenv()
bot = Bot(token=os.getenv("TG_TOKEN"))


async def main():
    """Running bot function"""
    dispatcher = Dispatcher(storage=MemoryStorage())

    dispatcher.include_router(common.router)
    dispatcher.include_router(detect_anime.router)

    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
