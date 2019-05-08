import os
from discord.ext import commands
import discord
import json, asyncio
import configparser
import traceback
import sys
import os
import re
import ast
import shutil
from pathlib import Path

token = 'bot token'

prefix = "!"

description = "!list" 



bot = commands.Bot(command_prefix=prefix, description=description)

@bot.command(hidden=True)
async def list(ctx):
    await ctx.send(embed, "Emoticons list\n**.**")
  
bot.run(token)
