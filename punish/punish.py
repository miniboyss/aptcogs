import discord
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
from typing import Any

Cog: Any = getattr(commands, "Cog", object)

class PunishCog(Cog):
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="punish")
    async def _punish(self, ctx, user: discord.User):
        """Punish a user by quarantining them to a specified channel. If the quarantine role does not exist, it will be created."""

        #role stuff
        guild = ctx.guild
        perms = discord.Permissions(send_messages=False, read_messages=True)
        await guild.create_role(name="Quarantined", perms)
        role = get(guild.roles, name="Quarantined")
        await user.add_roles(role)

        #channel stuff
        channel = get(guild.channels, name="quarantine")
        if channel is None:
            await guild.create_text_channel("quarantine")
        channel = get(guild.channels, name="quarantine")
        await channel.set_permissions(role, send_messages=True)
        channel.send(f"{user}, you may only talk here now.")

def find_pings(text):
    """returns a list of ids"""
    char1 = "<@!"
    char12 = "<@"
    char2 = ">"
    char1ins = find_substring(char1, text)
    if len(char1ins) == 0:
        char1 = "<@"
        char1ins = find_substring(char12, text)
    char2ins = find_substring(char2, text)
    #if len(char1ins) == 0 or len(char2ins) == 0:
    #    return None
    ids = []
    for k, v in enumerate(char1ins):
        try:
            char2ins[k]
        except:
            break
    
        ids.append(text[char1ins[k]+len(char1):char2ins[k]])
    return ids
