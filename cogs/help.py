from datetime import datetime
import discord
from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.ext import commands


class Help(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.command(name="ping")
    async def fun(self, ctx):
        await ctx.send(f"Pong {round(self.bot.latency*1000, 1)} ms!")   

    @commands.command(name="help")
    async def help_command(self, ctx):
        
        embed=Embed(title="HELP", description="Welcome to the Subdroid help dialog! \n Prefix = sub", color=0x15cb55, timestamp=datetime.utcnow())
        embed.add_field(name="----Info----", value="Subdroid is a chatting bot. He has bunch of custom and automacitated messages that you can play around with. He also can find something on wikipeida for you! Just try him out! Commands are below.")
        embed.add_field(name="-----Commands-----", value="```droid``` - when you type subdroid [content] to chat with subdroid. When you type ```subdroid Do you know about|what is|who is|tell me about [content]``` he will find [content] on wikipedia for you. \n ```ping``` - ping command", inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help dialog initiated")

def setup(bot):
    bot.add_cog(Help(bot))