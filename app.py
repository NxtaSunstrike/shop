import asyncio
import logging

from aiogram import Bot,Dispatcher
from bot.handlers import admin, user, payment
from bot.databases.base import async_main

from bot.web_apps.shop.app import alive
from bot.commands.shop_com import setup_bot_commands
from bot.middlewares.check_in import CheckSubs

logging.basicConfig(level=logging.INFO)

async def main()->None:
    await async_main()
    
    bot = Bot(token = "7021625991:AAEjiUjvdOVuHQMyJKlJfuaxgZL-zLn1YVk")
    dp = Dispatcher()
    await setup_bot_commands(bot=bot)

    dp.message.middleware(CheckSubs())
    dp.include_routers(user.router,admin.router,payment.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

        
    except Exception as _ex:
        pass

alive()
if __name__ == '__main__':
    asyncio.run(main()) 
    
    
