import discord
from discord.utils import get

from discord import channel
from discord import role

#This token has been disabled
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
        #if you want to use a custom emoji on your server you will need to find it's name and id and put it in the format <:name:id>
        emoji = "<:ellie:740572588819873793>"
        await message.add_reaction(emoji)

client.run(TOKEN)
