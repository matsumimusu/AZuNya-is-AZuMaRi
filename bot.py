import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
client = bot


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == '01':
        await message.channel.send(f"**USER : **<@{message.author.id}>我在喔")
@bot.command()
async def i(ctx):
    await ctx.send(f"圖片系統(施工中)")
@bot.command()
async def j(ctx):
    await ctx.send(f"笑話系統(施工中)")
@bot.command()
async def l(ctx):
    await ctx.send(f"伺服器經驗系統(施工中)")
@bot.command()
async def m(ctx):
    await ctx.send(f"音樂系統(施工中)")
@bot.command()
async def t(ctx):
    await ctx.send(f"小工具系統(施工中)")




@bot.event 
async def on_ready():
    print(">>安ニャーsay yooo~~~<<")

import json
with open('items.json', "r", encoding = "utf8") as file:
    data = json.load(file)
    bot.run(data['token']) 