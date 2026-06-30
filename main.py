from bot.bot import bot
from bot.uploader import Uploader
import asyncio


async def main() : 
    Bot = bot()
    uploader = Uploader(Bot)
    await Bot.start()
    

asyncio.run(main())