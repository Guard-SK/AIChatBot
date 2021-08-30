import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test", guild_ids=807971983081472000, description="This is a test")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="embed test")
        await ctx.send(content="test", embeds=[embed])

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slash initiated")

def setup(bot):
    bot.add_cog(Slash(bot))