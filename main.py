# Aiogram
import asyncio
from aiogram.filters.command import Command
from aiogram import F

# Local
from settings import dp, bot
import handlers as hs
import constants as const


dp.message.register(hs.hello, Command('start')) # register handlers
dp.message.register(hs.dialog, hs.ModuleFSM.gpt) # register handlers
dp.message.register(hs.help, Command('help'))
dp.message.register(hs.default, F.text) 


async def main():
    """Start bot in asynchronius function."""
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main()) # start async main

