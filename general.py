import discord
import random
from discord.ext import commands
import embedlinks

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message, amount=1):
        channel = self.client.get_channel(734034302555127808)
        if message.author.id == 298424256075792385:
            await channel.purge(limit=amount)


    @commands.command()
    async def fortuneball(self, ctx, * , question):
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

    @commands.command()
    async def beat(self, ctx, member : discord.Member):
        author = ctx.message.author
        await ctx.send(f'Ouch, {author.mention} has beaten the shit out of {member.mention}.')

    @commands.command()
    async def fban(self, ctx, *, member):
        await ctx.send(f'**SIKE, YOU THOUGHT YOU CAN BAN IDIOT!** {ctx.author.mention}')

    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(
        colour = discord.Colour.dark_red(),
        description="Hello! I am the Soviet Commissar. I am a test bot of my creator, val̸̒̏ȯ̸̿r̸͊͑#0001. I may only be seen in my creator's test server. Enjoy your day!"
        )
        embed.set_author(name="Soviet Commissar", icon_url="https://media.discordapp.net/attachments/439758640782508032/739008319338971176/technobladee.jpg")

        await ctx.send(embed=embed)

    @commands.command()
    async def waifu(self, ctx):
        chosen_image = random.choice(embedlinks.waifulinks)

        embed = discord.Embed(
        colour = discord.Colour.red()
        )

        embed.set_author(name="Kawaii!", icon_url="https://media.discordapp.net/attachments/733991528854454322/739652132931895387/fujiwara.gif")
        embed.set_image(url=chosen_image)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f"{ctx.author.avatar_url}")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(General(client))
