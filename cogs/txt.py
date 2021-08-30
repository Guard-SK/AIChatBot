from collections import namedtuple
from datetime import datetime
import discord
from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.ext import commands
from random import choice


class CustomChat(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="droid hi", aliases=["droid hello", "droid ciao"])
    async def hi(self, ctx):
        Embed=discord.Embed(name="Subdroid")
        await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya', 'Sup', 'Ciao', '<:peepohey:806962515152994406>'))} {ctx.author.mention}!")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Custom chat initiated")

def setup(bot):
    bot.add_cog(CustomChat(bot))