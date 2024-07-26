# Zombot
A really stupid discord bot that I use with my Project Zomboid server because I don't want to buy a static ip and pz doesn't accept ddns domain names as ip.

# How to run (Linux)
You need to input your discord bot token and channel id where you want the thing to send messages.
On linux when executing in terminal you need to tell the system to use python using [python3 Zombot.py], no brackets, no quotation marks.
I sugest creating a blank text file and imputing python3 Zombot.py and setting it as executeable. (or just put #!/usr/bin/env python3 in the first line)

# Alternative way to run
Using this method requires import os and channel and token lines of the code that are comented by default to be uncomented, they replace the uncomented lines of the code.
This allows for easier changing of the channel id and bot token.

export DISCORD_TOKEN='your_discord_token'
export CHANNEL_ID='your_channel_id'
python3 Zombot.py
