# -*- coding: utf-8 -*-    
import os
from discord.ext import commands
import discord
import json, asyncio
import traceback
import sys
import os
import re
import ast
import shutil
from pathlib import Path

prefix = [
    ',',
    '?',
]

description = '?list'

bot = commands.Bot(command_prefix=prefix, description=description)
bot.dir_path = os.path.dirname(os.path.realpath(__file__))
bot.command_list = []


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

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/1.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e2(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/2.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e3(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/3.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e4(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/4.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e5(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/5.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e6(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/6.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e7(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/7.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e8(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/8.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e9(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/9.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e10(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/10.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e11(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/11.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e12(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/12.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e13(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/13.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e14(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/14.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e15(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/15.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e16(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/16.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e17(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/17.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e18(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/18.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e19(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/19.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e20(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/20.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e21(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/21.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e22(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/22.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e23(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/23.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e24(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/24.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e25(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/25.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e26(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/26.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e27(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/27.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e28(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/28.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e29(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/29.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e30(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/30.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e31(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/31.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e32(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/32.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e33(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/33.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e34(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/34.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e35(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/35.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e36(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/36.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e37(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/37.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e38(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/38.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e39(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/39.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e40(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/40.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e41(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/41.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e42(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/42.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e43(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/43.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e44(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/44.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e45(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/45.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e46(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/46.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e47(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/47.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e48(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/48.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e49(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/49.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e50(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/50.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e51(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/51.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e52(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/52.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e53(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/53.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e54(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/54.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e55(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/55.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e56(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/56.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e57(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/57.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e58(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/58.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e59(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/59.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e60(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/60.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e61(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/61.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e62(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/62.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e63(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/63.png")
    await ctx.send(embed=embed)
    
@bot.command(hidden=False)
async def e64(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/64.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e65(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/65.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e66(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/66.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e67(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/67.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e68(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/68.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e69(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/69.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e70(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/70.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e71(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/71.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e72(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/72.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e73(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/73.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e74(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/74.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e75(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/75.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e76(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/76.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e77(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/77.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e78(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/78.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e79(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/79.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e80(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/80.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e81(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/81.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e82(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/82.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e83(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/83.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e84(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/84.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e85(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/85.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e86(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/86.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e87(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/87.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e88(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/88.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e89(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/89.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e90(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/90.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e91(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/91.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e92(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/92.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e93(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/93.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e94(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/94.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e95(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/95.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e96(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/96.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e97(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/97.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e98(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/98.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e99(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/99.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e100(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/100.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e101(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/101.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e102(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/102.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e103(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/103.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e104(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/104.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e105(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/105.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e106(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/106.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e107(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/107.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e108(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/108.png")
    await ctx.send(embed=embed)

@bot.command(hidden=False)
async def e109(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url="https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/109.png")
    await ctx.send(embed=embed)

# Execute

bot.run('NTczNDUyODkwMTM2Mzc5Mzk1.XMrEJQ.z0oxL1bUXJzAFZKkPUT2Ubjcefo')
