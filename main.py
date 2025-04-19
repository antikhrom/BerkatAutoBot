import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Вставь сюда свой токен бота
TOKEN = "8193630010:AAEfYsNTX0T1qcdttCBTfP2b6aZcevSOvxI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.answer("Привет! Я работаю!")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())