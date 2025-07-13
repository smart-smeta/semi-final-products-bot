from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start_handler(message: Message):
    await message.answer("👋 Привет! Добро пожаловать в наш бот доставки еды.\nНажми /menu чтобы начать заказ.")

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.register(start_handler, commands={"start"})

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
