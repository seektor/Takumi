import os
import random

import discord
from discord.errors import LoginFailure
from discord.ext import commands
from dotenv import load_dotenv

from cogs.dictionary import DictionaryCogs
from cogs.listeners import ListenerCogs
from cogs.selection import SelectionCogs

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.add_cog(ListenerCogs(bot))
bot.add_cog(SelectionCogs(bot))
bot.add_cog(DictionaryCogs(bot))

bot.run(TOKEN)
