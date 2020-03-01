import discord
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
import requests
import json
from typing import Any

Cog: Any = getattr(commands, "Cog", object)

class MimicCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.serverURL = "http://localhost:4583/"

    @commands.command(name="mimic", alias="")
    async def _mimic(self, ctx, message):
        await ctx.send(f"{message}")