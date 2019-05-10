# -*- coding: utf-8 -*-    

import os
from discord.ext import commands
import discord
import datetime
import json, asyncio
import copy
import configparser
import traceback
import sys
import os
import re
import ast
import shutil
from pathlib import Path

import config

# sets working directory to bot's folder
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

token = config.token
prefix = config.prefix
description = config.description

bot = commands.Bot(command_prefix=prefix, description=description)
bot.dir_path = os.path.dirname(os.path.realpath(__file__))
bot.command_list = []

def get_command_list():
    bot.command_list = []
    for command in bot.commands:
        bot.command_list.append(command.name)
        bot.command_list.extend(command.aliases)
        
bot.get_command_list = get_command_list

@bot.check # taken and modified from https://discordpy.readthedocs.io/en/rewrite/ext/commands/commands.html#global-checks
async def globally_block_dms(ctx):
    if ctx.guild is None:
        raise discord.ext.commands.NoPrivateMessage('test')
        return False
    return True

# mostly taken from https://github.com/Rapptz/discord.py/blob/async/discord/ext/commands/bot.py. Taken directly from https://github.com/nh-server/kurisu and slightly edited. License below.
   # Copyright {yyyy} {name of copyright owner}


   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at


       # http://www.apache.org/licenses/LICENSE-2.0


   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass  # ...don't need to know if commands don't exist
    elif isinstance(error, discord.ext.commands.NoPrivateMessage):
        await ctx.send("You cannot use this command in DMs!")
    elif isinstance(error, discord.ext.commands.errors.BadArgument):
        await ctx.send("You provided a bad argument. Please double check your arguments, and try again.")
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        formatter = commands.formatter.HelpFormatter()
        await ctx.send("You are missing required arguments.\n{}".format(formatter.format_help_for(ctx, ctx.command)[0]))
    elif isinstance(error, discord.ext.commands.errors.CheckFailure):
        await ctx.send("You don't have permission to use this command.")
    else:
        if ctx.command:
            await ctx.send("An error occurred while processing the `{}` command.".format(ctx.command.name))
        print('Ignoring exception in command {0.command} in {0.message.channel}'.format(ctx))
        tb = traceback.format_exception(type(error), error, error.__traceback__)
        error_trace = "".join(tb)
        print(error_trace)
        if bot.log_channel:
            embed = discord.Embed(description=error_trace)
            await bot.log_channel.send("An error occurred while processing the `{}` command in channel `{}`.".format(ctx.command.name, ctx.message.channel), embed=embed)

@bot.event
async def on_error(event_method, *args, **kwargs):
    if isinstance(args[0], commands.errors.CommandNotFound):
        return
    print("Ignoring exception in {}".format(event_method))
    tb = traceback.format_exc()
    error_trace = "".join(tb)
    print(error_trace)
    if bot.log_channel:
        embed = discord.Embed(description=error_trace)
        await bot.log_channel.send("An error occurred while processing `{}`.".format(event_method), embed=embed)
        
# end Apache licensing.


@bot.event
async def on_ready():
    for guild in bot.guilds:
        try:
            bot.guild = guild
                
            bot.creator = discord.utils.get(guild.members, id=177939404243992578)
            
            bot.log_channel = discord.utils.get(guild.channels, id=486994270620876830)
            bot.ignored_channels = {bot.log_channel}
            for id in config.ignored_chans:
                bot.ignored_channels.add(discord.utils.get(guild.channels, id=id))
                
            bot.spoiler_role = discord.utils.get(guild.roles, id=409749833176580097)
            bot.direct_role = discord.utils.get(guild.roles, id=421417111169138712)
            bot.staff_role = discord.utils.get(guild.roles, id=349851767078649859)
            bot.mute_role = discord.utils.get(guild.roles, id=385493119233163265)
                
            bot.message_purge = False
            
            get_command_list()
                
            if not Path("saves/bot_status.json").exists():
                print("saves/bot_status.json doesn't exist. Creating from sample file")
                try:
                    shutil.copy("saves/bot_status.json.sample", "saves/bot_status.json")
                except:
                    print("saves/bot_status.json.sample doesn't exist. Please download from repo.")
            else:
                with open('saves/bot_status.json', 'r') as f:
                    status = json.load(f)
                    
                if status["status"] == "game":
                    await bot.change_presence(activity=discord.Game(name=status["presence"]))
                elif status["status"] == "music":
                    await bot.change_presence(activity=discord.Activity(name=status["presence"], type=discord.ActivityType.listening))
                elif status["status"] == "watch":
                    await bot.change_presence(activity=discord.Activity(name=status["presence"], type=discord.ActivityType.watching))
                
            if not Path("saves/warns.json").exists():
                print("saves/warns.json doesn't exist. Creating from sample file")
                try:
                    shutil.copy("saves/warns.json.sample", "saves/warns.json")
                    bot.load_extension('addons.warn')
                except:
                    print("saves/warns.json.sample doesn't exist. Please download from repo.")
            if not Path("saves/fwinfo.json").exists():
                print("saves/fwinfo.json doesn't exist. Creating from sample file")
                try:
                    shutil.copy("saves/fwinfo.json.sample", "saves/fwinfo.json")
                except:
                    print("saves/fwinfo.json.sample doesn't exist. Please download from repo.")
            if not Path("saves/mutes.json").exists():
                print("saves/mutes.json doesn't exist. Creating from sample file")
                try:
                    shutil.copy("saves/mutes.json.sample", "saves/mutes.json")
                except:
                    print("saves/mutes.json.sample doesn't exist. Please download from repo.")
            
            print("Initialized on {}.".format(guild.name))
        except Exception as e:
            print("Failed to initialize on {}".format(guild.name))
            print("\t{}".format(e))


@bot.command()
async def reload(ctx):
    """Reloads an addon."""
    if ctx.author != ctx.guild.owner and ctx.author != bot.creator:
        return await ctx.send("You can't use this!")
    errors = ""
    for addon in os.listdir("addons"):
        if ".py" in addon:
            addon = addon.replace('.py', '')
            try:
                bot.unload_extension("addons.{}".format(addon))
                bot.load_extension("addons.{}".format(addon))
            except Exception as e:
                errors += 'Failed to load addon: `{}.py` due to `{}: {}`\n'.format(addon, type(e).__name__, e)
    if not errors:
        bot.get_command_list()
        await ctx.send(':white_check_mark: Extensions reloaded.')
    else:
        await ctx.send(errors)
        
@bot.command(hidden=True)
async def botedit(ctx, *, name=""):
    """Edits the bot profile. Takes name only, at the moment. Bot owner only"""
    if ctx.author != bot.creator:
        return
    if not name:
        name = bot.user.name
    return await bot.user.edit(username=name)

@bot.command(hidden=False)
async def list(ctx):
    embed = discord.Embed(title="**List of Emoticons**", description="1:???\n2:거 말 존나 많네 씨발련이!!!!\n3:호에에에에\n4:예 축하드리구요\n5:이것은 개발자가 높게 평가\n6:머쓱\n7:와 정말 알고싶던 내용 이었어요 감사합니다! ^^\n8:그걸믿었음? 플라잉킥!!\n9:머래씨발 로타게작작봐\n10:허,,,미~ ~쓉,,,팔\n11:말을 잇지 못하는....\n12:응!! 그건 니가 못해서 그런거야!\n13:힝힝8ㅅ8\n14:하긴 니같은 대갈텅텅씨발썅간나새끼가 뭘알겠니?\n15:ㅎㅎ, 저에 어둠인격에 그만\n16:구라야 ㅎ\n17:혼모노다 혼모노\n18:그럼 게임끄고 잠이나 자지 왜 하니?쉬바롬이...\n19:당근빳다죠쉬바\n20:대신귀여운루돌프를드리겠습니다\n21:싸우지말고 몬던해\n22:아니!!!!쫌!!!마!!!!\n23:로사엔 그런문화가 있나보군요\n24:마짱뜨까? 어? 뜨까?\n25:뭘 쪼개는것이지? 개발자따라 돌은것인가?ㅋㅋ\n26:크흑....감사합니다 MASTER\n27:한심\n28:맹독 한사바리 머글래요?\n29:설마,, 유없찐?? 킥킥\n30:아 너무 무섭다\n31:와.. 맛잇겟다..\n32:니가 투사라니 이 겜 수준도 참 알만하다\n33:으겍 퉷퉷퉷 쓉창엠창\n34:진자 땡큐함니다\n35:유없찐??킥킥\n36:우와!! 정말데단해!\n37:판사는 저는 시각장애입미다\n38:쫑긋 아리송..\n39:이게 몬 게소리지?\n40:님은 안대요 ㅎ\n41:나만 템업소...\n42:호고곡;;; 님들 이새끼 프미에요!\n43:미친녀나!!!!\n44:안뇽안뇽!!\n45:너 진짜 미친년이지 어 !!!!??\n46:사기캐련~ ~\n:47쒸,,,불,,,룐,,,ㅎㅎ\n48:싢러요 않대요!!\n49:ㅇㄱㄹㅇㅋㅋㅋ\n50:근성이 부족해 근성이 쉬발아\n51:옘병하고있내\n52:거기에 너까지 죽었으면 완벽했을텐데...\n53:ㄹㅇ루??\n54:끼에에에엑!!!!!!!오지는 지랄발강!\n55:별룬대요? 흠..\n56:로창섹기 꺼저\n57:개깝추시내요\n58:지랄이 상당하시내요\n59:저건 진짜 사람이 아니다 사이버 망령이지\n60:스미마셍 스미마셍\n61:그렇게 돈이 좋냐 이 돈의 노예야\n62:그래서 오쪼라구요?\n63:듣고보니 그럿네?\n64:내 맞워요!~!\n65:내.. 다음 환자분..\n67:나와\n68:나오라했다\n69:이게 대체 뭐자? 이것 보세요 윽 역겨워\n70:딱히 틀린 얘기도 아닌듯 해서 수긍했다.\n71:에이 설마 또 안되겠냐? 넌럭키짱~\n72:냥냥 푸뤩휅꾸이익>이라는..\n73:그건 또 뭔.. 야 너 문과지\n74:너.. 이런겜 하니?..\n75:그냥 니가 손이 딸린거라고 정직하게 말하십시오\n76:그걸믿었음?플라잉킥!!\n77:제대로함\n78:3:0\n79:와우 리을리?\n80:저딴망겜 대체 누가 하는지 ㅎㅎㅋ\n81:꼬우면 꺼지등가 ㅎ\n82:이녀석 몬던충이에요 제가 밨서요\n83:!!\n84:싸우지말고 몬던해\n85:으아악미친 씹놈이다\n86:응 니네아빠 신술없어서 강림씀\n87:이기어검에서이기빼주세요\n88:왜냐하면..이기는 쫌금.. 일●충 같으니깐..ㅎ\n89:메피충 극혐이다 ㅋㅋ\n90:밸런스를 왜 여기서 구하실까?\n91:끼요오오옷ㅅㅅㅇ\n92:인생을 살아주세요..\n93:술을 넘모 만이 마셧나바요~\n94:아닌데요?\n95:호에에에에에에ㅔ에에에\n96:잘했서요~\n97:저기요 미친놈씨\n98:제발 강화터진소리 자제부탁드립니다\n99:잘자...\n100:허걱스\n101:쒸,,,불,,,룐,,,ㅎㅎ\n102:셀프박제 오지네\n103:일단은 쳐맞고 시작해 볼까?\n104:?????\n105:그걸 말이라구 해!!\n106:냄세나\n107:보감~\n108:이거 동의?\n109:우리 여보가 자야 나도 자요..\n**usage: !e[number]\nex) !e33**", color=0xffffff)
    await ctx.send(embed=embed)
@bot.command(hidden=False)
async def e1(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/1.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e2(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/2.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e3(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/3.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e4(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/4.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e5(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/5.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e6(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/6.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e7(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/7.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e8(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/8.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e9(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/9.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e10(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/10.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e11(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/11.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e12(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/12.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e13(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/13.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e14(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/14.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e15(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/15.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e16(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/16.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e17(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/17.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e18(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/18.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e19(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/19.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e20(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/20.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e21(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/21.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e22(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/22.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e23(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/23.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e24(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/24.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e25(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/25.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e26(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/26.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e27(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/27.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e28(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/28.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e29(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/29.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e30(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/30.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e31(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/31.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e32(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/32.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e33(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/33.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e34(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/34.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e35(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/35.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e36(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/36.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e37(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/37.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e38(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/38.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e39(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/39.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e40(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/40.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e41(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/41.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e42(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/42.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e43(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/43.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e44(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/44.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e45(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/45.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e46(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/46.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e47(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/47.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e48(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/48.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e49(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/49.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e50(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/50.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e51(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/51.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e52(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/52.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e53(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/53.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e54(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/54.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e55(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/55.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e56(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/56.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e57(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/57.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e58(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/58.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e59(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/59.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e60(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/60.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e61(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/61.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e62(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/62.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e63(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/63.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e64(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/b5e2a1bf604260ed7d9078fe06cc399f1a07187a/_data/64.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e65(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/65.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e66(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/66.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e67(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/67.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e68(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/68.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e69(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/69.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e70(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/70.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e71(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/71.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e72(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/72.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e73(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/73.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e74(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/74.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e75(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/75.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e76(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/76.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e77(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/77.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e78(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/78.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e79(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/79.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e80(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/80.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e81(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/81.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e82(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/82.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e83(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/83.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e84(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/84.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e85(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/85.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e86(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/86.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e87(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/87.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e88(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/88.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e89(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/89.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e90(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/90.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e91(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/91.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e92(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/92.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e93(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/93.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e94(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/94.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e95(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/95.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e96(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/96.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e97(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/97.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e98(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/98.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e99(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/99.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e100(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/100.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e101(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/101.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e102(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/102.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e103(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/103.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e104(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/104.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e105(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/105.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e106(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/106.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e107(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/107.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e108(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/108.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e109(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/hexdc.github.io/master/_data/109.png")
    await ctx.send(embed=embed)

# Execute
print('Bot directory: ', dir_path)
bot.run(token)
