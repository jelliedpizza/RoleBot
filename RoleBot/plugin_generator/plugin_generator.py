import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
if not os.path.exists("plugins_generated"):
    os.makedirs("plugins_generated")

def num1():
    command_name = input('What commnad should initiate the process (only letters, numbers and underscores anything else will resoult in an error): ')
    amount = int(input("How many emojis/roles will you need (Enter a number): "))
    message = input("Please specify the message that the reactions will go on (Explain by clicking which emoji they revice which role and what does the role do and that this is permanent): ")
    emojis = []
    roles = []
    print("\n")
    for i in range(amount):
        emoji = input(f"Enter trigger emoji {i+1}/{amount} (Since you can't type emojis in the terminal/commandprompt use the 'charinfo' command while the bot is running and than the emoji to recive the code to enter here, don't worry this is the last time you your emoji in this form, the first emoji will be paired up with the first role and the second with the second and so on.): ")
        if ":" in emoji:
            splitted = emoji.split(":")
            emoji = f"discord.utils.get(self.bot.get_all_emojis(), id='{splitted[1]}')"
        else:
            emoji = "'" + emoji + "'"

        emojis.append(emoji)
    for i in range(amount):
        role = input(f"Enter role {i+1}/{amount} that the user will recive(The first emoji you entered will be paired up with the first role and the second with the second and so on.): ")
        roles.append(role)
    
    add_emojis = ""
    for i in emojis:
        add_emojis += f'        await self.bot.add_reaction(msg, {i})\n'

    add_roles = ""
    first = 1
    for anemoji, arole in zip(emojis, roles):
        if first == 1:
            add_roles += f"""            if res.reaction.emoji == {anemoji}:\n                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='{arole}'))\n"""
            first = 0
        else:
            add_roles += f"""            elif res.reaction.emoji == {anemoji}:\n                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='{arole}'))\n"""

    
    normalliststr = "["
    for i in range(emojis.__len__() - 1):
        num = i
        normalliststr += emojis[num] + ", "
    normalliststr += emojis[-1] + "]"
    wfe = normalliststr.replace("\\\\", "\\")

    final = f"""import discord
from discord.ext import commands
import checks
import asyncio

class {command_name}():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='{command_name}', pass_context=True)
    async def choice(self, ctx):
        '''{message}'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('{message}')
{add_emojis}
        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction({wfe}, message=msg)
{add_roles}

def setup(bot):
    bot.add_cog({command_name}(bot))"""

    print("\n")
    if os.path.isfile(f"plugins_generated/{command_name}.py"):
        print("File with that init command alredy exists")
        return
    else:
        f = open(os.path.join("plugins_generated", command_name + ".py"), "w+")
        f.write(final)
    print("Plugin created in the 'plugins_generated' folder with the name of the name of the command as the filename.")
    return

def num2():
    command_name = input('What commnad should initiate the process (only letters, numbers and underscores anything else will resoult in an error): ')
    amount = int(input("How many emojis/roles will you need (Enter a number): "))
    message = input("Please specify the message that the reactions will go on (Explain by clicking which emoji they revice which role and what does the role do and that this is permanent): ")
    emojis = []
    roles = []
    print("\n")
    for i in range(amount):
        emoji = input(f"Enter trigger emoji {i+1}/{amount} (Since you can't type emojis in the terminal/commandprompt use the 'charinfo' command while the bot is running and than the emoji to recive the code to enter here, don't worry this is the last time you your emoji in this form, the first emoji will be paired up with the first role and the second with the second and so on.): ")
        if ":" in emoji:
            splitted = emoji.split(":")
            emoji = f"discord.utils.get(self.bot.get_all_emojis(), id='{splitted[1]}')"
        else:
            emoji = "'" + emoji + "'"

        emojis.append(emoji)
    for i in range(amount):
        role = input(f"Enter role {i+1}/{amount} that the user will recive(The first emoji you entered will be paired up with the first role and the second with the second and so on.): ")
        roles.append(role)
    
    add_emojis = ""
    for i in emojis:
        add_emojis += f'        await self.bot.add_reaction(msg, {i})\n'

    add_roles = ""
    first = 1
    for anemoji, arole in zip(emojis, roles):
        if first == 1:
            add_roles += f"""            if res.reaction.emoji == {anemoji}:\n                await self.bot.remove_reaction(msg, {anemoji}, res.user)\n                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='{arole}'))\n"""
            first = 0
        else:
            add_roles += f"""            elif res.reaction.emoji == {anemoji}:\n                await self.bot.remove_reaction(msg, {anemoji}, res.user)\n                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='{arole}'))\n"""

    
    normalliststr = "["
    for i in range(emojis.__len__() - 1):
        num = i
        normalliststr += emojis[num] + ", "
    normalliststr += emojis[-1] + "]"
    wfe = normalliststr.replace("\\\\", "\\")

    final = f"""import discord
from discord.ext import commands
import checks
import asyncio

class {command_name}():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='{command_name}', pass_context=True)
    async def choice(self, ctx):
        '''{message}'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('{message}')
{add_emojis}
        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction({wfe}, message=msg)
{add_roles}

def setup(bot):
    bot.add_cog({command_name}(bot))"""

    print("\n")
    if os.path.isfile(f"plugins_generated/{command_name}.py"):
        print("File with that init command alredy exists")
        return
    else:
        f = open(os.path.join("plugins_generated", command_name + ".py"), "w+")
        f.write(final)
    print("Plugin created in the 'plugins_generated' folder with the name of the name of the command as the filename.")
    return

def num3():
    command_name = input('What commnad should initiate the process (only letters, numbers and underscores anything else will resoult in an error): ')
    message = input("Please specify the message that the reactions will go on (Explain by clicking which emoji they receive which role and what does the role do and that they can undo this action): ")
    role = input("what role should the users be able to controll: ")
    emoji_add = input("What emoji adds the role to the user (Since you can't type emojis in the terminal/commandprompt use the 'charinfo' command while the bot is running and than the emoji, to recive the code to enter here, don't worry this is the last time you your emoji in this form): ")
    if ":" in emoji_add:
        splitted = emoji_add.split(":")
        emoji_add = f"discord.utils.get(self.bot.get_all_emojis(), id='{splitted[1]}')"
    else:
        emoji_add = "'" + emoji_add + "'"
    emoji_remove = input("What emoji removes the role from the user (Since you can't type emojis in the terminal/commandprompt use the 'charinfo' command while the bot is running and than the emoji, to recive the code to enter here, don't worry this is the last time you your emoji in this form): ")
    if ":" in emoji_remove:
        splitted = emoji_remove.split(":")
        emoji_remove = f"discord.utils.get(self.bot.get_all_emojis(), id='{splitted[1]}')"
    else:
        emoji_remove = "'" + emoji_remove + "'"

    final = f"""import discord
from discord.ext import commands
import checks
import asyncio

class {command_name}():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='{command_name}', pass_context=True)
    async def {command_name}(self, ctx):
        '''{message}'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('{message}')
        await self.bot.add_reaction(msg, {emoji_add})
        await self.bot.add_reaction(msg, {emoji_remove})
        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction([{emoji_add}, {emoji_remove}], message=msg)
            if res.reaction.emoji == {emoji_add}:
                await self.bot.remove_reaction(msg, {emoji_add}, res.user)
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name="{role}"))
            elif res.reaction.emoji == {emoji_remove}:
                await self.bot.remove_reaction(msg, {emoji_remove}, res.user)
                await self.bot.remove_roles(res.user, discord.utils.get(msg.server.roles, name="{role}"))

def setup(bot):
    bot.add_cog({command_name}(bot))"""

    print("\n")
    if os.path.isfile(f"plugins_generated/{command_name}.py"):
        print("File with that init command alredy exists")
        return
    else:
        f = open(os.path.join("plugins_generated", command_name + ".py"), "w+")
        f.write(final)
    print("Plugin created in the 'plugins_generated' folder with the name of the name of the command as the filename.")
    return

print("Hey, this should help you making plugins for RoleBot:")
print("You have to chose from these three base configurations")
print("\n[1]:    Basic Multiple Choice\nWith the use of an iniciating command the bot will send a message to the channel that you sent the command in \nand will react with one or more emojis of your choosing. Any user who clicks a reaction will recive a role specified by you based on what emoji they click, this is irreversible and the reaction counter will not reset.")
print("\n[2]:    Multiple Choice with reseting\nWith the use of an iniciating command the bot will send a message to the channel that you sent the command in \nand will react with one or more emojis of your choosing. Any user who clicks a reaction will recive a role specified by you based on what emoji they click, this is irreversible and the reaction counter will reset.")
print("\n[3]:    Add-Remove \nWith the use of an iniciating command the bot will send a message to the channel that you sent the command in \nand will react with two emojis of your choosing. Any user who clicks the first reaction will recive a role specified by you and if they click the other the role will be removed from them and the reaction counter will reset.")

while True:
    num = int(input('Enter a number: '))
    print("\n")
    if num == 1:
        num1()
        break
    elif num == 2:
        num2()
        break
    elif num == 3:
        num3()
        break
    else:
        print("You entered an invalid number")
print("Task finished; press RETURN to exit.")
input("")