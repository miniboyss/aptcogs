from redbot.core.bot import Red
from .mimic import MimicCog

def setup(bot: Red):
    bot.add_cog(MimicCog(bot))
