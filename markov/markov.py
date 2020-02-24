import discord
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
from typing import Any
from .markovgen import MarkovGen

Cog: Any = getattr(commands, "Cog", object)

class MarkovCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.markov = MarkovGen(open('text.txt'))

    @commands.command(name="markov_test", alias="")
    async def _test(self, ctx):
        print("test")

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('text.txt', "a+") as f:
            f.write(message.content+"\n")

        if message.startswith("hey minebot"):
            await message.channel.send(self.markov.generate_markov_text())

        
