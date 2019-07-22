from redbot.core.bot import Red
from .stickyroles import StickyRolesCog

def setup(bot: Red):
    bot.add_cog(StickyRolesCog(bot))
