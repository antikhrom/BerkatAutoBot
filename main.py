from aiogram import Bot, Dispatcher, types, executor
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я работаю!")

if __name__ == "__main__":
    executor.start_polling(dp)
