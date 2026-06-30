import os 
from bot.bot import bot
import asyncio


class Uploader : 
    def __init__(self , bot:bot):
        self.bot = bot

    async def upload_all_files_in_dir(self ,user ,  dir) : 
        works = [ ]
        for root,dirs,files in os.walk(dir) : 
            for file in files : 
                works.append(self.bot.send_file(user ,os.path.join(root, file)))
        
        await asyncio.gather(*works)