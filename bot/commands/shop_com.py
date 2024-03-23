from aiogram import Bot

from aiogram.types import BotCommand


async def setup_bot_commands(bot:Bot)->None:
    bot_commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get info about me"),
        BotCommand(command="/orders", description="Your orders"),        
    ]
    await bot.set_my_commands(bot_commands)