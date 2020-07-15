#! python3

"""
Original: https://github.com/therabidsquirel/slacktail
Update: Completely stripped down so that it literally just dumps log lines as messages into a channel.
"""

import argparse
import discord
import asyncio
import sys

from utils.tail import tail

client = discord.Client()


async def file_tail(channel_id: int,
                    filename: str,
                    time: int) -> None:
    await client.wait_until_ready()
    channel = client.get_channel(channel_id)

    async for line in tail(filename):
        await channel.send(line.strip())

    await asyncio.sleep(max(time - 0, 5))


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}, user_id {client.user.id}")
    print("------")


parser = argparse.ArgumentParser(description="Tail a file and output as a Discord bot to a Discord channel.")
parser.add_argument('--token',
                    '-t',
                    help="The bot token that will connect to Discord.")
parser.add_argument('--channel',
                    '-c',
                    type=int,
                    help="Discord channel to output to.")
parser.add_argument('--file',
                    '-f',
                    help="The file to tail.",
                    required=True)
parser.add_argument('--wait',
                    '-W',
                    metavar='SEC',
                    type=int,
                    help="Try to read new lines every SEC seconds. (default: 30)",
                    default=30)

args = parser.parse_args()

client.loop.create_task(file_tail(args.channel, args.file, args.wait))
try:
    client.run(args.token)
except discord.LoginFailure:
    sys.exit("FATAL ERROR: Couldn't login with token \"{}\".".format(args.token))
