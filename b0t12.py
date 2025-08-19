import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

TOKEN = "8042770659:AAH-fAQ6IeyuBLExbWUBKOhYTcU8BGjAcVU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопка для открытия Mini App
@dp.message(commands=["start"])
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Открыть Mini App 🚀",
                web_app=WebAppInfo(url="https://твоя-ссылка.github.io/")
            )]
        ]
    )
    await message.answer("Привет! Жми кнопку и откроется мини-приложение 👇", reply_markup=keyboard)


# Обработка данных из Mini App
@dp.message()
async def handle_webapp(message: types.Message):
    if message.web_app_data:
        data = message.web_app_data.data
        await message.answer(f"📩 Получены данные из Mini App:\n{data}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
