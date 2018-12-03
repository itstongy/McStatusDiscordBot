import discord
from mcstatus import MinecraftServer as mc


TOKEN = ''
SERVERIP = ''

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!status'):
        server = mc.lookup(SERVERIP)
        status = server.status()
        players =""
        if status.players.sample is not None:
            for player in status.players.sample:
                players+= '\n ' + str(player.name)
        else:
            players="No players online"
        msg = ("The Server has {}/{} players online. \n{}".format(
            status.players.online,
            status.players.max,
            str("```" + players + "```")
            ))
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
