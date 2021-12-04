import discord
from discord.utils import get

from discord import channel
from discord import role

TOKEN = "OTE1OTg0NjIxNjcyNDY4NTMw.YajjJw._fw2jeLHOM6ZFr3S4rHLBoGAUQ0"

client = discord.Client()


@client.event
async def on_ready():
    print("logged in")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    userroles = message.author.roles

    role = discord.utils.find(
        lambda r: r.name == 'women', message.guild.roles)

    if role in userroles:
        print("woman detected")
        emoji = "<:ellie:740572588819873793>"
        await message.add_reaction(emoji)

client.run(TOKEN)
