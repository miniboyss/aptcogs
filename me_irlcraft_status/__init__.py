from redbot.core.bot import Red
from .status import StatusCog

def setup(bot: Red):
    bot.add_cog(StatusCog(bot))
