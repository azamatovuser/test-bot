from aiogram import Bot, Dispatcher
import asyncio
from handlers import start_router, button_handlers_router

bot = Bot(token='7434111701:AAGAdYAWZNNdsPyKouOFXq5O5A0UmtTzcLg')
dp = Dispatcher(bot=bot)


async def main():
    dp.include_routers(start_router,
                       button_handlers_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())