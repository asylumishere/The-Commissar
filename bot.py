import discord
import random
import os
from discord.ext import commands
from discord.ext import tasks
import asyncio
import embedlinks

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready.")
    await client.change_presence(activity=discord.Game(name="with some commands."))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to do that!")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This is not a command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("There are missing arguments.")
    if isinstance(error, commands.BadArgument):
        await ctx.send("There are missing arguments.")

    raise error

@client.command()
async def help(ctx):
    embed = discord.Embed(
     colour=discord.Colour.dark_purple()
    )
    embed.set_author(name="Commands")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/733991796799045683/736460006718963752/technobladee.jpg")
    embed.add_field(name="help", value="`Shows this message.`", inline=False)
    embed.add_field(name="fortuneball", value="`It shows your fortune.`")
    embed.add_field(name="mod", value="`Shows moderator commands.`", inline=False)
    embed.add_field(name="beat", value="`Beat the shit out of someone.`")
    embed.set_footer(text="Created by [REDACTED]", icon_url="https://media.discordapp.net/attachments/439758640782508032/739310715323809798/1fd4a1952514b759f4695a04892a9a2b.gif")
    await ctx.send(embed=embed)

@client.command()
@commands.has_guild_permissions(manage_guild=True)
async def mod(ctx):
    author = ctx.message.author
    embed = discord.Embed(
     colour=discord.Colour.dark_red()
    )
    embed.set_author(name="Moderator Commands")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/733991796799045683/736460006718963752/technobladee.jpg")
    embed.add_field(name= "`mod`", value= "`Shows this message.`", inline=False)
    embed.add_field(name="`kick`", value="`Kick Command.`")
    embed.add_field(name="`ban`", value="`Ban Command.`", inline=False)
    embed.add_field(name="`purge`", value="`Deletes messages.`")
    embed.add_field(name="`send`", value="`Sends a message to everyones' direct messages.`", inline=False)
    embed.add_field(name="`activity`", value="`Sends an activity check.`")
    embed.set_footer(text="Created by [REDACTED]", icon_url="https://media.discordapp.net/attachments/439758640782508032/739310715323809798/1fd4a1952514b759f4695a04892a9a2b.gif")
    await author.send(embed=embed)
    await ctx.send(f'Check your DMs! {author.mention}')

@client.command()
@commands.has_guild_permissions(manage_guild=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f"Loaded {extension}")

@client.command()
@commands.has_guild_permissions(manage_guild=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')    
    print(f"Unloaded {extension}")

@client.command()
@commands.has_guild_permissions(manage_guild=True)
async def activity(ctx):
     channel = client.get_channel(734034368691175485)
     await channel.send("@everyone Activity Check!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzMzOTg0MzAxNjk5MzAxNDM4.XxL0iA.SDTAZNUegOyiW_tttucDGeqbKWY")
