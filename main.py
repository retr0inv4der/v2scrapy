from bot.bot import bot
import asyncio


async def main() : 
    Bot = bot()
    await Bot.start()
    

asyncio.run(main())