#Import des librairies
import discord
import configparser

#Initialisation de ConfigParser
config = configparser.ConfigParser()
config.read("config.ini")

#Key configparser
tokenBot = config['DEFAULT']['TOKENBOT']

#Connexion du bot
client = discord.Client()
client.run(tokenBot)