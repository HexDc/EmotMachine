# -*- coding: utf-8 -*-    
import os
from discord.ext import commands
import discord
import sys
import os
import config
prefix = [
    '?',
    ';',
]

description = '!list'
link = 'https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/'
bot = commands.Bot(command_prefix=prefix, description=description)


@bot.command(hidden=False)
async def list(ctx):
    embed = discord.Embed(title="**List of Emoticons**", description=config.descript, color=0xffffff) 
    await ctx.send(embed=embed)
@bot.command(hidden=False)
async def e1(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "1.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e2(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "2.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e3(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url=link + "3.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e4(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url=link + "4.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e5(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url=link + "5.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e6(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "6.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e7(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "7.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e8(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "8.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e9(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "9.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e10(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "10.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e11(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "11.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e12(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "12.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e13(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "13.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e14(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "14.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e15(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "15.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e16(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "16.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e17(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "17.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e18(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "18.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e19(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "19.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e20(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "20.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e21(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "21.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e22(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "22.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e23(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "23.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e24(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "24.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e25(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "25.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e26(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "26.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e27(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "27.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e28(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "28.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e29(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "29.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e30(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "30.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e31(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "31.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e32(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "32.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e33(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "33.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e34(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "34.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e35(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "35.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e36(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "36.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e37(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "37.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e38(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "38.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e39(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "39.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e40(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "40.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e41(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "41.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e42(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "42.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e43(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "43.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e44(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "44.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e45(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "45.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e46(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "46.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e47(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "47.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e48(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "48.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e49(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "49.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e50(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "50.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e51(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "51.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e52(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "52.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e53(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "53.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e54(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "54.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e55(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "55.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e56(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "56.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e57(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "57.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e58(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "58.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e59(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "59.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e60(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "60.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e61(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "61.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e62(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "62.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e63(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "63.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e64(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "64.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e65(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "65.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e66(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "66.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e67(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "67.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e68(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "68.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e69(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "69.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e70(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "70.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e71(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "71.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e72(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "72.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e73(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "73.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e74(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "74.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e75(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "75.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e76(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "76.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e77(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "77.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e78(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "78.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e79(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "79.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e80(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "80.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e81(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "81.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e82(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "82.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e83(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "83.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e84(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "84.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e85(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "85.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e86(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "86.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e87(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "87.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e88(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "88.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e89(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "89.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e90(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "90.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e91(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "91.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e92(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "92.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e93(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "93.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e94(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "94.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e95(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "95.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e96(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "96.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e97(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "97.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e98(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "98.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e99(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "99.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e100(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "100.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e101(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "101.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e102(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "102.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e103(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "103.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e104(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "104.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e105(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "105.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e106(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "106.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e107(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "107.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e108(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "108.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e109(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "109.png")
    await ctx.send(embed=embed)

bot.run('token')
