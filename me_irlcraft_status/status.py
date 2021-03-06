import discord
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
import requests
import json
from typing import Any

Cog: Any = getattr(commands, "Cog", object)

class StatusCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.serverURL = "http://localhost:4583/"

    @commands.command(name="players", alias="")
    async def _players(self, ctx):
        r = requests.get(self.serverURL+"players")
        players = json.loads(r.text)

        playerString = ""

        for player in players['players']:
            playerString = playerString+player+"\n"
        await ctx.send(f"There are {players['count']} players on.```md\n{playerString}```")