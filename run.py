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

    await (await bot.ws.ping())

    now = datetime.datetime.now()

    return now - msgtime
  
bot.run(token)
