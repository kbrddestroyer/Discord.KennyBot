import discord
from discord.ext import commands

import os

# Создаем бота
Bot = commands.Bot(
    intents=discord.Intents.default(),
    command_prefix="!"
)

@Bot.event
async def on_message(ctx):
    print(ctx)
    if ctx.author != Bot.user:
        await ctx.reply("Bruh")
    
config = {
    'token': os.environ['TOKEN']
}

Bot.run(config['token'])

