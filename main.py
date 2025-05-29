from aiogram import Bot, Dispatcher
import asyncio
from bot import bot_router
from admin import admin_router
from database import Base, engine
from configs import TELEGRAM_API_TOKEN
# TODO токен
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()
Base.metadata.create_all(bind=engine)
from database.otherservice import *

# TODO это нужно убрать после теста
try:
    add_admin_info("t.me/Dark_Just")
    add_channel("https://t.me/JustCrypto_X", -1002110888721)
except:
    pass

async def main():
    dp.include_router(bot_router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())