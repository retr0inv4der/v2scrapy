from bot.bot import bot
import asyncio


async def main() : 
    Bot = bot()
    await Bot.start()
    await Bot.send_msg("me" , "test1")

asyncio.run(main())