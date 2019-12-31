import discord
from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        """Simple response to test if bot is functioning."""
        await ctx.send('pong!')
