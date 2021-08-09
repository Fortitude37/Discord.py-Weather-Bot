from discord.ext.commands import Cog
from discord import requests
from glob import glob
class WeatherBasic(Cog):
        def __init__(self, bot):
            self.bot = bot
        self._last_member = None
        api_key = "948f3a72d132f94de83639735ce9e983"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        @client.command()
        async def weather(ctx, *, city: str):
            city_name = city
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            channel = ctx.message.channel
            if x["cod"] != "404":
                    async with channel.typing():
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_temperature_celsiuis = str(round(current_temperature - 273.15))
                        current_pressure = y["pressure"]
                        current_humidity = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        weather_description = z[0]["description"]
                        embed = discord.Embed(title=f"Weather in {city_name}",
                                color=ctx.guild.me.top_role.color,
                                timestamp=ctx.message.created_at,)
                        embed.add_field(name="Description", value=f"**{weather_description}**", inline=False)
                        embed.add_field(name="Temperature(Celsius)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
                        embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                        embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
                        embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                        embed.set_footer(text=f"Requested by {ctx.author.name}")
                        await channel.send(embed=embed)
            else:
                await channel.send("City not found.")

class Fun(Cog):
    def __intit__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("commands ready")
        print("commands ready")

def setup(bot):
    bot.add_cog(Fun(bot))
    
