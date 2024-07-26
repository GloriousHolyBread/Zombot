#import os
import discord
import requests
import asyncio
from discord.ext import commands, tasks

#DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
#CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

DISCORD_TOKEN = 'TOKEN'
CHANNEL_ID = CHANNEL

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

ip_address = None

@tasks.loop(minutes=10)
async def check_ip_change():
    global ip_address
    channel = bot.get_channel(CHANNEL_ID)
    
    if channel is None:
        print(f"Channel with ID {CHANNEL_ID} not found")
        return

    try:
        response = requests.get('https://api.ipify.org?format=json')
        new_ip = response.json().get('ip')
        
        if ip_address is None:
            await channel.send("The IP is the same")
        elif ip_address != new_ip:
            await channel.send(f"The IP address has changed. New IP: {new_ip}")
            
        ip_address = new_ip
    except Exception as e:
        print(f"Error checking IP: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    check_ip_change.start()

@bot.command(name='ip')
async def send_ip(ctx):
    global ip_address
    if ip_address:
        await ctx.send(f"Current IP address: {ip_address}")
    else:
        await ctx.send("IP address not yet determined.")

bot.run(DISCORD_TOKEN)
