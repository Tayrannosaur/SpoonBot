import os

import discord
from discord.ext import commands
import dotenv

from .util import Util
from .fun  import Fun

def launch():
    try:
        TOKEN = os.environ['SPOONBOT_TOKEN']
    except KeyError:
        print("Could not launch: Didn't find a login token!")

    description = '''This is a custom bot for Clara_The_Classy's Discord server!'''

    bot = commands.Bot(command_prefix='~', description=description)

    bot.add_cog(Util(bot))
    bot.add_cog(Fun(bot))


    bot.run(TOKEN)
