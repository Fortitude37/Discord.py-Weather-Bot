from glob import glob
from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.errors import CommandNotFound
from discord.ext.commands import CommandNotFound
from ..db import db
from apscheduler.triggers.cron import CronTrigger

PREFIX= "+"
OWNER_IDS = [204529741225525248]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/.py")]

class Bot(BotBase):
    def __init__(self):
        
        self.PREFIX = PREFIX
        self.ready = False 
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        
        db.autosave(self.scheduler)
        super().__init__(
            command_prefix = PREFIX,
             owner_ids=OWNER_IDS,
             intents=Intents.all(),
             )

    def setup(self):
        for cog in COGS:
            self.load_extension(f".lib.cogs.{cog}")
            print(f" {cog} cog loaded")
            print("setup complete")

    def run(self, version):
        self.VERSION = version

        print("running setup...")
        self.setup()
        print("done setup")

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running")
        super().run(self.TOKEN, reconnect=True)

    async def print_message(self):
        
        await self.stdout.send("time notification")

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
            self.stdout = self.get_channel(851864375479762994)
            #temp
            #self.scheduler.add_job(self.print_message, CronTrigger(hour= "0,15,30,45"))
            #self.scheduler.start()
            

            await self.stdout.send("bot online")

            # embed = Embed(title="online", description="bot is online", color=0xFF0001)
            # embed.add_field(name="NAME", value="Value", inline=True)
            # fields = [("Name", "Value", True),
            #         ("another field", "idk what this does", True),
            #         ("none-inline field", "appear on its own row", False)]
            # for name, value, inline in fields:
            #     embed.add_field(name=name, value=value, inline=inline) 
            # await channel.send(embed=embed)

            print("ready")

        else:        

            print("reconnected")
    
    async def on_message(self, message):
        pass

bot = Bot()