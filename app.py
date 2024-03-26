import asyncio
import logging

from aiogram import Bot,Dispatcher
from bot.handlers import admin, user, payment
from bot.databases.base import async_main


from bot.commands.shop_com import setup_bot_commands
from bot.middlewares.check_in import CheckSubs

logging.basicConfig(level=logging.INFO)
from flask import Flask,render_template
from bot.databases.requests import get_cloths,get_cloth_by_id
from threading import Thread

app = Flask(__name__)


@app.route('/')
async def index():
    cloths = await get_cloths()
    return render_template('main_page.html',cloths = cloths,enumerate=enumerate)


@app.route('/<int:id>')
async def cloth(id):
    cloth = await get_cloth_by_id(id=id)
    return render_template('cloth.html',enumerate = enumerate,cloth = cloth)


def run():
    app.run(host='0.0.0.0', port=8080)


def alive():
  t = Thread(target=run)
  t.start()

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
    
    
