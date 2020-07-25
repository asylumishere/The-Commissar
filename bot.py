import discord
import random
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready.")
   
@client.command(aliases=['Help'])
async def help(ctx):
    embed = discord.Embed(
     colour=discord.Colour.orange()
    )
    embed.set_author(name="Commands")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/733991796799045683/736460006718963752/technobladee.jpg")
    embed.add_field(name="help", value="`Shows this message.`", inline=False)
    embed.add_field(name="fortuneball", value="`It shows your fortune.`")
    embed.add_field(name="ping", value="`Shows your latency.`", inline=False)
    embed.add_field(name="fban", value="`It's maybe a ban...`")
    embed.add_field(name="mod", value="`Shows moderator commands.`", inline=False)
    embed.add_field(name="beat", value="`Beat the shit out of someone.`")   
    embed.set_footer(text="Created by val̸̒̏ȯ̸̿r̸͊͑#2774", icon_url="https://images-ext-1.discordapp.net/external/fsiz3ER16gezLXfgDY7TM9-EWRjFfxVOPZXaCgrJ3K4/%3Fsize%3D256/https/cdn.discordapp.com/avatars/298424256075792385/08d6b28a6baa8725778d0558a7da59c6.png")
    await ctx.send(embed=embed)
    
@commands.has_permissions(manage_guild=True)
@client.command()
async def mod(ctx):
    embed = discord.Embed(
     colour=discord.Colour.blue()
    )
    embed.set_author(name="Moderator Commands")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/733991796799045683/736460006718963752/technobladee.jpg")
    embed.add_field(name="`mod`", value="`Shows this message.`", inline=False)
    embed.add_field(name="`kick`", value="`Kick Command.`")
    embed.add_field(name="`ban`", value="`Ban Command.`", inline=False)
    embed.add_field(name="`purge`", value="`Deletes messages.`")
    embed.set_footer(text="Created by val̸̒̏ȯ̸̿r̸͊͑#2774", icon_url="https://images-ext-1.discordapp.net/external/fsiz3ER16gezLXfgDY7TM9-EWRjFfxVOPZXaCgrJ3K4/%3Fsize%3D256/https/cdn.discordapp.com/avatars/298424256075792385/08d6b28a6baa8725778d0558a7da59c6.png")
    await ctx.send(embed=embed)
    
  

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def fortuneball(ctx, * , question):
    responses = [
    'Don’t count on it.',
    'Ask again later.',
    'Better not tell you now.',
    'Concentrate and ask again.',
    'As I see it, yes.',
    'It is certain.',
    'Most likely.',
    'My reply is no.',
    'My sources say no.',
    'It is decidedly so.',
    'Outlook good.',
    'Outlook not so good.',
    'Very doubtful.',
    'Reply hazy, try again.',
    'Without a doubt.',
    'Signs point to yes.',
    'You may rely on it.',
    'My reply is no.',
    'Yes - definitely.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@commands.has_permissions(manage_messages=True)
@client.command()
async def purge(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Your opinion doesnt matter...')
     
@commands.has_permissions(manage_guild=True)
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'You will never come back here... {member.mention}')

@commands.has_permissions(manage_guild=True)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Get deleted... {member.mention}')
    
@client.command()
async def fban(ctx, *, member):
    await ctx.send('**SIKE, YOU THOUGHT YOU CAN BAN IDIOT!**')
    
@client.command()
async def beat(ctx, member : discord.Member):
    author = ctx.message.author
    await ctx.send(f'Ouch!, {author.mention} has beaten the shit out of {member.mention}.')    

client.run('NzM0NTkyNDM4NjAxMTIxODQy.XxUadA.SRhaMLqN75KB_n7SuJez5OlPm5w')
