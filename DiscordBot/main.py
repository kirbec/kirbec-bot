import discord
from DiscordClient import DiscordClient
import os

# from dotenv import load_dotenv

# load_dotenv()

# Main script to start the DiscordClient
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = DiscordClient(intents=intents)
client.run(DISCORD_TOKEN)
