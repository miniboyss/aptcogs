from redbot.core.bot import Red
from .punish import PunishCog

def setup(bot: Red):
    bot.add_cog(PunishCog(bot))
