import discord
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
from typing import Any

Cog: Any = getattr(commands, "Cog", object)

class MarkovCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        print(message)
