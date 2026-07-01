import os
from bot.bot import bot
from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.tl.types import Channel
from telethon.types import Message

class Handler : 
    def __init__(self , bot : bot):
        self.bot = bot
        self.client = self.bot.client

    def register(self) : 
        self.client.add_event_handler(self.on_new_message , NewMessage)

    async def on_new_message(self , event:Message) : 
        
        if event.is_channel : 
            sender:Channel = await event.get_sender()
            if sender is not None : 
                title = getattr(sender, "title", getattr(sender, "username", "unknown"))
            print(title + ":  " + event.message.message)