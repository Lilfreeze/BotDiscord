#Import des librairies
#import discord
from discord.ext import commands
import configparser
import random

#Initialisation de ConfigParser
config = configparser.ConfigParser()
config.read("config.ini")

#Key configparser
tokenBot = config['DEFAULT']['TOKENBOT']

#Connexion du bot
#client = discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready !")

@bot.command(name="jeux")
async def ping(ctx: commands.Context):
    await ctx.send(jeux())


@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()

    for each_message in messages:
        await each_message.delete()

#client.run(tokenBot)
bot.run(tokenBot)