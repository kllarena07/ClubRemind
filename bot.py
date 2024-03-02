import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
import asyncio
load_dotenv()

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command()
async def create_event(ctx, date_str, time_str, *, reminder):
    try:
        event_date = datetime.datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
        current_time = datetime.datetime.now()
        time_difference = event_date - current_time
        if time_difference.total_seconds() < 0:
            await ctx.send("Invalid date or time. Event should be scheduled for a future time.")
            return
        
        await asyncio.sleep(time_difference.total_seconds())
        await ctx.send(f"Reminder: {reminder}")
    except ValueError:
        await ctx.send("Invalid date or time format. Please use YYYY-MM-DD HH:MM format.")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
