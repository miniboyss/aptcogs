import discord
from discord.ext import commands
from redbot.core import Config, checks, commands
from discord.utils import get
from typing import Any

Cog: Any = getattr(commands, "Cog", object)

class PunishCog(Cog):
    """A cog that handles quarantining."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="quarantine", alias="")
    async def _punish(self, ctx, user: discord.User):
        """Punish a user by quarantining them to a specified channel. If the quarantine role does not exist, it will be created."""
        guild_perms = ctx.message.author.guild_permissions
        if guild_perms.manage_messages == False:
            await ctx.send("You don't have permission.")
            return
        #role stuff
        guild = ctx.guild
        role = get(guild.roles, name="Quarantined")
        if role is None:
            await guild.create_role(name="Quarantined")
        role = get(guild.roles, name="Quarantined")
        member = guild.get_member(user.id)
        await member.add_roles(role)
        
        for channel in guild.channels:
            await channel.set_permissions(role, send_messages=False)

        #channel stuff
        channel = get(guild.channels, name="quarantine")
        if channel is None:
            await guild.create_text_channel("quarantine")
        channel = get(guild.channels, name="quarantine")
        await channel.set_permissions(role, send_messages=True)
        await channel.send(f"<@!{user.id}>, you may only talk here now.")
        await ctx.send(f"<@!{user.id}> quarantined successfully.")
        await ctx.send("https://giphy.com/gifs/ban-banned-admin-fe4dDMD2cAU5RfEaCU"