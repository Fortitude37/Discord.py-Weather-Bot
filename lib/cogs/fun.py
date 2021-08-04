from discord.ext.commands import Cog
from glob import glob

class Fun(Cog):
    def __intit__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("commands ready")
        print("commands ready")

def setup(bot):
    bot.add_cog(Fun(bot))
    