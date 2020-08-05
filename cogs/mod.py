import discord
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 734034368691175485:
            await message.add_reaction("✅")

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def send(self, ctx, *, args):
     if args !=None:
        members = ctx.guild.members
        embed = discord.Embed(
        colour = discord.Colour.dark_red()
        )
        embed.set_author(name="The Krieg Dynasty", icon_url="https://media.discordapp.net/attachments/707487147434967143/739012212802322492/giphy_5_cropped.gif")
        embed.add_field(name="Message from High Command", value=(args))
        embed.set_footer(text="Created by [REDACTED]", icon_url="https://media.discordapp.net/attachments/439758640782508032/739310715323809798/1fd4a1952514b759f4695a04892a9a2b.gif")
        for member in members:
            try:
                await member.send(embed=embed)
                await ctx.send(f"Successfully Dmed : {member} :white_check_mark: ")
            except:
                print("can't")
                await ctx.send(f"Unable to send Dm to : {member} :x: ")

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} messages deleted.")

    @commands.command()
    @commands.has_guild_permissions(manage_guild=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}. Reason: {reason}")

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}. Reason: {reason}")

def setup(client):
    client.add_cog(Mod(client))
