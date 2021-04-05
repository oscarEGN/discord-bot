import discord
from discord.ext import commands
import time
import math
import os
#import googletrans
#from googletrans import Translator
from dotenv import load_dotenv

client = commands.Bot(command_prefix="#")

time = time.asctime()

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def sub(x: float, y: float):
    return x - y

def add(x: float, y: float):
    return x + y

def div(x: float, y: float):
    return x / y

def sqrt(x: float):
    return math.sqrt(x)

@client.event
async def on_ready():
    print("Le bot est prêt")

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "Aucune raison fournie"):
    await member.send("Vous avez été kick du serveur, a cause de:"+reason)
    await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "Aucune raison fournie"):
    await ctx.send(member.name + "a été banni du serveur, a cause de:"+reason)
    await member.ban(reason=reason)

@client.command()
async def mathadd(ctx, x: float, y: float):
    res = add(x, y)
    await ctx.send(res)

@client.command()
async def mathsub(ctx, x: float, y: float):
    res = sub(x, y)
    await ctx.send(res)

@client.command()
async def mathdiv(ctx, x: float, y: float):
    res = div(x, y)
    await ctx.send(res)

@client.command()
async def mathsqrt(ctx, x: int):
    res = sqrt(x)
    await ctx.send(res)

client.run(token)