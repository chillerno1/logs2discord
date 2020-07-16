import argparse
import discord
import asyncio
import sys

client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}, user_id {client.user.id}")
    print("------")
    print("Listing available channels:")
    print("------")

    for channel in client.get_all_channels():
        if channel.type.name != 'category':
            print(f"name:{channel.name}, id: {channel.id}, type:{channel.type}")

    await client.close()

parser = argparse.ArgumentParser(description="List available channel ids for Discord server.")
parser.add_argument('--token',
                    '-t',
                    help="The bot token that will connect to Discord.")

args = parser.parse_args()

try:
    client.run(args.token)
except discord.LoginFailure:
    sys.exit("FATAL ERROR: Couldn't login with token \"{}\".".format(args.token))
