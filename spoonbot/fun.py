import discord
from discord.ext import commands
import httpx

from .random_img import random_img

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def laffy(self, ctx):
        """Fetches a terrible joke in the spirit of laffy taffy puns."""
        headers = {'accept': 'text/plain'}
        joke = await httpx.get('https://icanhazdadjoke.com/', headers=headers)
        await ctx.send(joke.text)
        
    @commands.command()
    async def wwmd(self, ctx):
        """What would miku do? Provides you with vocaloid wisdom."""
        response = await httpx.get('https://api.adviceslip.com/advice')
        advice = response.json()['slip']['advice']
        await ctx.send('Miku says: ' + advice)

    @commands.command()
    async def sora(self, ctx):
        """Gets a random picture of Sora Kingdom Hearts"""
        embed = discord.Embed()
        img = await random_img('sora')
        embed.set_image(url=img)
        await ctx.send(embed=embed)
