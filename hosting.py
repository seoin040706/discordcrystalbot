import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    game = discord.Game("!역할 요청 - 수정봇")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(' ')
    print('-----------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    print((bot.user.name) + ' - 작동중(Ready) feat.니이모 0: 00  ●━━━━━━─────── 04: 32 ⇆ㅤㅤㅤㅤ      ◁ㅤㅤ❚❚      ▷ㅤㅤㅤㅤ  ↻')
    print(' ')
    print(' ')
    print('-----------------------------------------------------------------------------------------------------------------------')
    print(' ')

@bot.event
async def on_message(message):
    if message.content.startswith('!역할 요청'):
        channel = message.channel
        embed = discord.Embed(title="역할 요청 성별",description="남성은 ♂ 여성은 ♀ 를 눌러서 역할을 적용할 수 있습니다.", color=0x00aaaa)
        embed.add_field(name="Man ♂", value="남성", inline=False)
        embed.add_field(name="Woman ♀", value="여성", inline=False)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("♂") #Man
        await msg.add_reaction("♀") #Woman

        def check(reaction, user):
            return user == message.author
            str(reaction.emoji) == '♂,♀'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('역할 요청 지속시간이 끝났습니다. 다시 요청하려면 ```!역할 요청```')
        else:
            if reaction.emoji == '♂':
                await channel.send('♂')
                role = discord.utils.get(message.guild.roles, name="남성")
                await message.author.add_roles(role)
                print((message.author.name) + '님이 남성 역할을 부여받았습니다.')
            if reaction.emoji == '♀':
                await channel.send('♀')
                role = discord.utils.get(message.guild.roles, name="여성")
                await message.author.add_roles(role)
                print((message.author.name) + '님이 여성 역할을 부여받았습니다.')

bot.run('NzY0MTA4MDYwNDA2NzEwMzIy.X4BdFg.bnzMAQpxx1V73h15AH58txUQpGA')