# logs2discord

Tails a log file and forwards output as message to discord channel.

## Requirements

 1. Discord bot with token
 2. discord Python package
 
## Install

 1. git clone this repo
 2. cd /where/its/cloned
 3. pip install -r requirements.txt
 
## Usage

Run in terminal:
```shell script
python3 logs2discord.py -t <token> -c <channel_id> -f <file_path> -W 15
```

Example:
```shell script
root@scriptbox: ~/logs2discord$ logs2discord.py -t 'XXXXXXXXXXXXX.XXXX.XXXXXXXXXXXXX' -c 732804641238809 -f '/var/log/syslog' -W 15
Logged in as logbot, user_id 73280464XXXXXXXX
------
```

## How do I get a channel_id?

Run in terminal:
```shell script
python3 channelinfo.py -t <token>
```

Example:
```shell script
root@scriptbox: ~/logs2discord$ python3 channelinfo.py -t 'XXXXXXXXXX.XXXXXX.XXXXXXXXXXX'
Logged in as logbot, user_id 73280464XXXXXXXX
------
Listing available channels:
------
name:general, id: 732805747XXXXXXXX, type:text
name:logs, id: 7328416557XXXXXXXX, type:text
```
