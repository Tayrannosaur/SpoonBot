import os

import discord
from discord.ext import commands
import dotenv

from .util import Util
from .fun  import Fun


def getToken():
    try:
        return os.environ['SPOONBOT_TOKEN']
    except KeyError:
        print("Could not launch: Didn't find a login token!")

def getPrefix():
    try:
        return os.environ['SPOONBOT_PREFIX']
    except KeyError:
        print("Could not launch: Didn't find a command prefix!")

def launch():
    token = getToken()
    prefix = getPrefix()

    description = '''This is a custom bot for Clara_The_Classy's Discord server!'''

    bot = commands.Bot(command_prefix=prefix, description=description)

    bot.add_cog(Util(bot))
    bot.add_cog(Fun(bot))


    bot.run(token)
