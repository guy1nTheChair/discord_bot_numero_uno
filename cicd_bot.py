import discord
from discord.ext import commands
import random

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

responses = [
    "fXGkfp",
    "dGX6Fw",
    "bnpoqe",
    "2RAHZR",
    "hZt7qt",
    "8LeAog",
    "m7vgw8",
    "Q5dhHv",
    "N6jkK8",
    "DaHCL6"
]

@client.event
async def on_ready():
    print("Bot is ready!!")


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server..sssup homiee!!')


@client.event
async def on_member_remove(member):
    print("kicked")
    print(f'{member} has left the server..adios homiee!!')


@client.command()
async def ping(ctx):
    await ctx.send("Pong after " + str(round(client.latency*1000,2)) + "ms")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(random.choice(responses))


@client.command()
async  def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} messages deleted!!')


@client.command()
async def kick(ctx, member: discord.Member, *, reason="you've been Kicked lmao!!"):
    #await member.kick(reason=reason)
    await ctx.send(f'{member} {reason}')


@client.command()
async def ban(ctx, member: discord.Member, *, reason="you've been Kicked lmao!!"):
    #await member.kick(reason=reason)
    await ctx.send(f'{member} {reason}')


@client.command()
async def unban(ctx, member: discord.Member, *, reason="you've been banned lmao!!"):
    print(client.users)
    print(type(ctx))
    #await member.ban(reason=reason)
    #await ctx.send(f'{member} {reason}')

client.run('Nzg2NjIzODU4ODgxOTg2NTcw.X9JGjg.Gqx7lCkfq5zfnEYoAJgg1fWxaSc')