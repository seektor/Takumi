import discord
from discord.ext import commands
from discord.ext.commands import errors


class ListenerCogs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        await ctx.send(f"There was an error: {err}")
