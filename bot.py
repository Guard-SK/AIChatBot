import discord
from discord import message
from discord.ext import commands
import wikipedia,os
from chatbot import Chat, register_call
from datetime import datetime
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown)
from discord.ext.commands.errors import MissingPermissions
from discord import Intents
from discord.errors import HTTPException, Forbidden
from discord.ext.commands import Bot as BotBase


intents = discord.Intents.default()
intents.members = True
prefix = "sub"
bot = commands.Bot(command_prefix = prefix, intents=intents)
COGS = [path[:-3] for path in os.listdir('./cogs') if path[-3:] == '.py']
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)


@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id == 544573811899629568:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cog(s) loaded.")

    else:
        await ctx.send(f"You are not the owner of the bot!!! GET OUT OF HERE!!! <:akaliNani:848283879826784286>")

@bot.command()
async def unload(ctx, extension):
    if ctx.message.author.id == 544573811899629568:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Cog(s) unloaded.")

    else:
        await ctx.send(f"You are not the owner of the bot!!! GET OUT OF HERE!!! <:akaliNani:848283879826784286>")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@register_call("whoIs")
def viki_sum(self, query):
    try:
        description = wikipedia.summary(query, auto_suggest=False)
        return description
    except Exception:
        return f"I don't know about *{query}*"
template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"CustomAnswers","chatbot.template")
chat=Chat(template_file_path)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/Guard-SK/Subdroid"))
    print("Subdroid started")

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         msg = f"<a:no_entry:826849755916140574>Cool down man <a:melting_ice:826761004980764702>. Try again in {error.retry_after:,.2f} secs.<a:no_entry:826849755916140574>"
#         await ctx.send(msg)

@bot.command(pass_context = True)
async def droid(ctx,*,message):
    result = chat.respond(message)
    if(len(result)<=2048):
        embed=discord.Embed(title="Subdroid", description = result, color = (ctx.author.color), timestamp=datetime.utcnow())
        await ctx.send(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="Subdroid", description = item, color = (ctx.author.color), timestamp=datetime.utcnow())
                embed.set_footer(text="Page {}".format(num))
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(description = item, color = (ctx.author.color), timestamp=datetime.utcnow())
                embed.set_footer(text = "Page {}".format(num))
                await ctx.send(embed = embed)

bot.run(os.environ['DISCORD_TOKEN']) # os.environ['DISCORD_TOKEN']