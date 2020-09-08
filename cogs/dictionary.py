import json
import os

import discord
import requests
from discord.ext import commands

from ..utils.utils import flat_map


class DictionaryCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.OXFORD_KEY = os.getenv('OXFORD_KEY')
        self.OXFORD_ID = os.getenv('OXFORD_ID')

    # via 'https://developer.oxforddictionaries.com/' Remember about proper app_key and app_id
    @commands.command()
    async def t_eng(self, ctx, *args):
        """Translates the following word to english"""

        language_code = 'en-gb'
        word = args[0]

        if not word:
            await ctx.send('Please provide a valid word')

        url = f"https://od-api.oxforddictionaries.com/api/v2/entries/{language_code}/{word}?fields=definitions"

        r = requests.get(
            url, headers={"app_id": self.OXFORD_ID, "app_key": self.OXFORD_KEY})
        r_json = r.json()

        if r.status_code != 200:
            embed = discord.Embed(colour=discord.colour.Color.red())
            error_msg = r_json['error'] or 'There has been a problem with the translation'
            embed.add_field(name='Error', value=error_msg)
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(colour=discord.colour.Color.blue())
        results_arr = r_json["results"]
        lexical_entries_arr = flat_map(
            lambda e: e["lexicalEntries"], results_arr)
        entries_arr = flat_map(lambda e: e["entries"], lexical_entries_arr)
        senses_arr = flat_map(lambda e: e["senses"], entries_arr)
        definitions_arr = flat_map(lambda e: e["definitions"], senses_arr)
        definitions = '\n'.join(definitions_arr)

        embed.add_field(name=f'{word.title()} definition', value=definitions)
        await ctx.send(embed=embed)
