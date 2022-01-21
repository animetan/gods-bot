import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@bot.event
async def on_ready():
    activity = discord.Game(name="𝐠 𝐨 𝐝 ' 𝐬 🎄", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

    



bot.run("OTMzNjY1Njc1NjYxMTU2Mzky.Yek16w.0iMAJ5KxGQ6co-kNdf8jCJW1nc8")