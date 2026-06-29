from bot.config import config
import os
from telethon import TelegramClient
from telethon.hints import EntityLike, MessageLike
import asyncio

class bot : 
    def __init__(self ):
        self.client = TelegramClient(config.botname , config.api_id , config.api_hash)

    async def start(self) : 
        try:
            await self.client.start()
        except :
            print("was not able to establish the connection with Telegram servers.")
            os.exit(1)
            
    async def send_msg(self , entity:EntityLike  , msg : MessageLike) : 
       await self.client.send_message(entity , msg)
       
    async def send_files(self,user ,  dir_path):
        paths = []
        works =[]
        for root,dirs,files in os.walk( dir_path): 
            for file in files :
                full_path = os.path.join(root , file)
                paths.append(full_path)
        for path in paths :
            works.append( self.client.send_file(user , path))
        await asyncio.gather(*works)