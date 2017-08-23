import discord
from discord.ext import commands
import checks
import asyncio

class test1():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='test1', pass_context=True)
    async def choice(self, ctx):
        '''test1'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('test1')
        await self.bot.add_reaction(msg, '\U0001f604')
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='345187162679017472'))

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['\U0001f604', discord.utils.get(self.bot.get_all_emojis(), id='345187162679017472')], message=msg)
            if res.reaction.emoji == '\U0001f604':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Member'))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='345187162679017472'):
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Super Member'))


def setup(bot):
    bot.add_cog(test1(bot))