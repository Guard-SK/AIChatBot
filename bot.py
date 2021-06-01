import discord
from discord import message
from discord.ext import commands
import wikipedia,os
from chatbot import Chat, register_call

intents = discord.Intents.default()
intents.members = True
prefix = "ai"
bot = commands.Bot(command_prefix = prefix, intents=intents)

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
    print("Project started")

@bot.command(pass_context = True)
async def chatbot(ctx,*,message):
    result = chat.respond(message)
    if(len(result)<=2048):
        embed=discord.Embed(title="ChatBot AI", description = result, color = (ctx.author.color))
        await ctx.send(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="ChatBot AI", description = item, color = (ctx.author.color))
                embed.set_footer(text="Page {}".format(num))
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(description = item, color = (ctx.author.color))
                embed.set_footer(text = "Page {}".format(num))
                await ctx.send(embed = embed)

bot.run(os.environ['DISCORD_TOKEN'])