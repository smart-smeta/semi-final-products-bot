import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from bot.keyboards.main import main_menu
from database.models import init_db, add_user

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start_handler(message: Message):
    user = message.from_user
    add_user(user.id, user.full_name, user.username or "")
    await message.answer(
        "👋 Привет! Добро пожаловать в бот доставки еды.\nВыберите действие:",
        reply_markup=main_menu
    )

async def main():
    init_db()

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.register(start_handler, CommandStart())

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
