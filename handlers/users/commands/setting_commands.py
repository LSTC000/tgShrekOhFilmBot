from data.messages import START_SHORT_MESSAGE

from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand(command='start', description=START_SHORT_MESSAGE)
        ]
    )
