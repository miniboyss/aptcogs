from redbot.core.bot import Red
from .markov import MarkovCog

def setup(bot: Red):
    bot.add_cog(MarkovCog(bot))
