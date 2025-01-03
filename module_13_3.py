from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


#записываем ключ
api = "7230751067:AAF4T2f8bkFK_iFPC9FfkK8UHPRT8wySgg8"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

#обработка сообщений хендлеры
@dp.message_handler(commands = ["Start"])
async def Start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ ==  "__main__":
    executor.start_polling(dp, skip_updates=True)
