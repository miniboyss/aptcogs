import discord
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
from typing import Any
import json

Cog: Any = getattr(commands, "Cog", object)

class StickyRolesCog(Cog):
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
        with open("data.json", "w+") as f:
            data = json.loads(f.read())
        