import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '^')

@client.event
async def on_ready():
    print("Bot is ready.")

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
client.run['NzM0NTkyNDM4NjAxMTIxODQy.XxUNlg.gs9EHNlwVn_CPAzXop2dEg6IEEE']
