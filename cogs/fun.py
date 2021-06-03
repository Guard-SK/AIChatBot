import asyncio
from random import randint, choice
from typing import Optional
from discord.errors import HTTPException
from aiohttp import request
from discord.ext import commands, tasks
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import cooldown
from discord.ext import commands
from datetime import datetime

import discord

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dice6", aliases=["roll6"])
    @cooldown(1, 10, BucketType.user)
    async def dice6(self, ctx):
        msg = await ctx.send("https://cdn.discordapp.com/attachments/629382706299666432/849733983234555994/1.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849734076880519179/5.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849734008883249162/3.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849734094111637514/6.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849734076880519179/5.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849733983234555994/1.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849734076880519179/5.png") 
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849733995909480511/2.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849734094111637514/6.png")
        await asyncio.sleep(0.50)
        await msg.edit(content="https://cdn.discordapp.com/attachments/629382706299666432/849734008883249162/3.png")
        await asyncio.sleep(0.50)
        await msg.delete()
        embed=discord.Embed(title="Result", description="------------>", color=ctx.author.color, timestamp=datetime.utcnow()) 
        embed.set_thumbnail(url=f"{choice(('https://cdn.discordapp.com/attachments/629382706299666432/849733983234555994/1.png', 'https://cdn.discordapp.com/attachments/629382706299666432/849733995909480511/2.png', 'https://cdn.discordapp.com/attachments/629382706299666432/849734008883249162/3.png', 'https://cdn.discordapp.com/attachments/629382706299666432/849734049689370664/4.png', 'https://cdn.discordapp.com/attachments/629382706299666432/849734076880519179/5.png', 'https://cdn.discordapp.com/attachments/629382706299666432/849734094111637514/6.png'))}")
        
        await ctx.send(embed=embed)

    @commands.command(name="flip", aliases=["coin"])
    @cooldown(1, 10, BucketType.user)
    async def flip_a_coin(self, ctx):
        await ctx.send(f"{choice(('https://cdn.discordapp.com/attachments/629382706299666432/850101854624808960/zh.gif', 'https://cdn.discordapp.com/attachments/629382706299666432/850101865874325514/zz.gif', 'https://cdn.discordapp.com/attachments/629382706299666432/850101876632715284/hz.gif', 'https://cdn.discordapp.com/attachments/629382706299666432/850101887982239824/hh.gif'))}")


    @commands.command(name="dice", aliases=["roll"])
    @commands.cooldown(1, 10, BucketType.user)
    async def roll_dice(self, ctx, die_string: str):
        dice, value = (int(term) for term in die_string.split("d"))

        if dice <= 100:
            rolls = [randint(1, value) for i in range(dice)]

            await ctx.send(" + ".join([str(r) for r in rolls]) + f" = {sum(rolls)}")
        
        else: 
            await ctx.send("Too many dice rolled. Please try lower number.")

    @roll_dice.error
    async def roll_dice_error(self, ctx, exc):
        if isinstance(exc.original, HTTPException):
            await ctx.send("Too many dice rolled. Please try lower number.")

    @commands.command(name="slap", aliases=["hit"])
    @cooldown(1, 5, BucketType.user)
    async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "no reason"):
        await ctx.send(f"{ctx.author.display_name} slapped {member.mention} for {reason}")

    @slap_member.error
    async def slap_member_error(self, ctx, exc):
        if isinstance(exc, BadArgument):
            await ctx.send("Can't find the memeber you mentioned.")

    @commands.command(name="say", aliases=["echo"])
    @cooldown(1, 5, BucketType.user)
    async def echo_message(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(name="fact")
    @cooldown(1, 10, BucketType.user)
    async def animal_fact(self, ctx, animal:str):
        if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):

            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'bird' if animal == 'bird' else animal}"

            async with request("GET", image_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]

                else:
                    image_link = None

            async with request("GET", fact_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    embed = Embed(title=f"{animal.title()} fact",
                                  description=data["fact"],
                                  color=ctx.author.color)
                    if image_link is not None:
                        embed.set_image(url=image_link)
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f"API returned a {response.status} status.")

        else:
            await ctx.send("No facts are available for that animal.")

    @animal_fact.error
    async def animal_fact_error(self, ctx, animal:str):
        pass

    @commands.command(name="dm", aliases=["direct message", "send"])
    async def send_dm(self, ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(content)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun initiated")

def setup(bot):
    bot.add_cog(Fun(bot))