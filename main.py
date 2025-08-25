import discord
from discord import app_commands
from discord.ext import commands
import os

TOKEN = os.environ["MTQwOTU3ODQ3NjkxODQwNzM4OA.GUDIpU.EbqSM0O1NJKIVZNSrT2kinoSQubKRoghqiqbGk"]  # https://discord.com/oauth2/authorize?client_id=1409578476918407388

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔗 Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

@bot.tree.command(name="send", description="Send a message 5 times")
@app_commands.describe(message="The message you want to repeat")
async def send(interaction: discord.Interaction, message: str):
    for _ in range(5):
        await interaction.channel.send(message)
    await interaction.response.send_message("✅ Message sent 5 times!", ephemeral=True)

bot.run(TOKEN)
