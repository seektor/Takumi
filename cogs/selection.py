import random

import discord
from discord.ext import commands

from utils.constants import EIGHT_BALL_ANSWERS


class SelectionCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yon(self, ctx):
        """Yes or No"""
        choices = ['Yes', 'No']
        await ctx.send(random.choice(choices))

    @commands.command()
    async def eight_ball(self, ctx):
        """Selects one from the 8ball answers"""
        answer = random.choice(EIGHT_BALL_ANSWERS)
        await ctx.send(answer)

    @commands.command()
    async def rate(self, ctx):
        """Selects random number between 0 - 10"""
        result = random.randrange(11)
        await ctx.send(result)

    @commands.command(aliases=['pick', 'choose'])
    async def select(self, ctx, *args):
        """Selects random element from the provided ones"""
        if(len(args) == 0):
            ctx.send("Please provide the list of options")
            return

        choice = random.choice(args)
        await ctx.send(choice)
