import discord
from discord.ext import commands

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

class PunishCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def _punish(self, ctx, name):
        """This does stuff!"""

        #Your code will go here
        text = find_pings(name)
        await ctx.send(text)

def setup(bot):
    bot.add_cog(Mycog(bot))