import discord
import markovify
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
from typing import Any

Cog: Any = getattr(commands, "Cog", object)

class MarkovCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.markov = None
        self.train()
        self.messageCounter = 0

    @commands.command(name="markov_test", alias="")
    async def _test(self, ctx):
        print("test")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 667544290309832714:
            return
        self.messageCounter = self.messageCounter + 1
        with open('text.txt', "a+") as f:
            f.write(message.content+"\n")

        if message.channel.id != 681648414311841813:
            return

        if "minebot" in message.content.lower():
            await message.channel.send(self.markov.make_sentence().replace("@", "@\\"))

        if self.messageCounter >= 100:
            print("reloading markov generator")
            self.train()
            self.messageCounter = 0

        
    def train(self):
        with open("text.txt") as f:
            text = f.read()
        self.markov = markovify.Text(text)