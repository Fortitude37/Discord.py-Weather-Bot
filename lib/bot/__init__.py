from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.errors import CommandNotFound
from discord.ext.commands import CommandNotFound
from ..db import db

PREFIX= "+"
OWNER_IDS = [204529741225525248]

class Bot(BotBase):
    def __init__(self):
        
        self.PREFIX = PREFIX
        self.ready = False 
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        
        db.autosave()
        super().__init__(
            command_prefix = PREFIX,
             owner_ids=OWNER_IDS,
             intents=Intents.all(),
             )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_commmand_error":
            await args[0].send("ruh roh.....")
        
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original
    
        else:   
            raise exc
            
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(360940298320216067)
            self.schedular.start()
            

            channel = self.get_channel(851864375479762994)
            await channel.send("bot online")

            # embed = Embed(title="online", description="bot is online", color=0xFF0001)
            # embed.add_field(name="NAME", value="Value", inline=True)
            # fields = [("Name", "Value", True),
            #         ("another field", "idk what this does", True),
            #         ("none-inline field", "appear on its own row", False)]
            # for name, value, inline in fields:
            #     embed.add_field(name=name, value=value, inline=inline)
                
            
            await channel.send(embed=embed)

            print("ready")

        else:        

            print("reconnected")
    
    async def on_message(self, message):
        pass

bot = Bot()