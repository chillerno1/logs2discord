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
