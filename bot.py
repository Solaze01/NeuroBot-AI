from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN
from services.gpt_service import get_gpt_reply

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: Message):
    user_input = message.text
    reply = await get_gpt_reply(user_input)
    await message.answer(reply)

if __name__ == "__main__":
    executor.start_polling(dp)
