import discord
from discord.ext import commands
import checks
import asyncio

class test3():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test3', pass_context=True)
    async def test3(self, ctx):
        '''test3'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('test3')
        await self.bot.add_reaction(msg, '\U0001f604')
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='345187162679017472'))
        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['\U0001f604', discord.utils.get(self.bot.get_all_emojis(), id='345187162679017472')], message=msg)
            if res.reaction.emoji == '\U0001f604':
                await self.bot.remove_reaction(msg, '\U0001f604', res.user)
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name="Super Member"))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='345187162679017472'):
                await self.bot.remove_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='345187162679017472'), res.user)
                await self.bot.remove_roles(res.user, discord.utils.get(msg.server.roles, name="Super Member"))

def setup(bot):
    bot.add_cog(test3(bot))