from bot.bot import bot
from bot.uploader import Uploader
from bot.handler import Handler
import asyncio


async def main() : 
    Bot = bot()
    uploader = Uploader(Bot)
    handler = Handler(Bot)
    handler.register()
    await Bot.start()
    

asyncio.run(main())