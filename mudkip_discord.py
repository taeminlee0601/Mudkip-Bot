import typing
import discord
import random
from discord.ext import commands
from discord.ext import tasks
import mudkip_dsc_class
from datetime import date
from datetime import datetime

description = '''Mudkip Bot Made By taemonster05#4520'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

user_tt = {}
late_start_days = [date(2023, 2, 15), date(2023, 2, 22), date(2023, 3, 22), date(2023, 3, 29), date(2023, 4, 19), date(2023, 4, 26), date(2023, 5, 24), date(2023, 5, 31)]


client = commands.Bot(command_prefix='!', description=description, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print(f' Logged on as {client.user} (ID: {client.user.id})')
    print('------------')

    await client.change_presence(activity=discord.Game('Trying to Evolve to Marshtomp!'))

@client.command()
async def genrandom(ctx, start: typing.Optional[int] = 1, end: typing.Optional[int] = 10):
    if start < end:
        randomNum = random.randint(start, end)
    elif end < start:
        await ctx.send("Start cannot be larger than end!")
        return

    await ctx.send("Your number from " + str(start) + "-" + str(end) + ": is " + str(randomNum))

@client.command()
async def settimetable(ctx, p1: str, p2: str, p3: str, p4: str):
    username = ctx.author.id
    user_tt[username] = mudkip_dsc_class.TimeTable(str(username), p1, p2, p3, p4)

@client.command()
async def stt(ctx, p1: str, p2: str, p3: str, p4: str):
    username = ctx.author.id
    user_tt[username] = mudkip_dsc_class.TimeTable(str(username), p1, p2, p3, p4)

@client.command()
async def timetable(ctx):
    today = date.today()

    username = ctx.author.id

    if user_tt.__contains__(username) is False:
        await ctx.send("Please enter your periods!")
        return

    passed = []

    for i in range(len(late_start_days)):
        if today > late_start_days[i]:
            passed.append(i)

    for i in reversed(passed):
        late_start_days.pop(i)

    await ctx.send(str(user_tt[username]))

@client.command()
async def tt(ctx):
    today = date.today()

    username = ctx.author.id

    if user_tt.__contains__(username) is False:
        await ctx.send("Please enter your periods!")
        return

    passed = []

    for i in range(len(late_start_days)):
        if today > late_start_days[i]:
            passed.append(i)

    for i in reversed(passed):
        late_start_days.pop(i)

    await ctx.send(str(user_tt[username]))

@client.command()
async def day(ctx):
    today = date.today()
    curDay = today.day

    if curDay % 2 == 0:
        await ctx.send("It is a Day 2")
    else:
        await ctx.send("It is a Day 1")

@client.command()
async def latestart(ctx):
    today = date.today()

    passed = []
    
    if len(late_start_days) == 0:
        await ctx.send("There are no more late starts!")

    for i in range(len(late_start_days)):
        if today > late_start_days[i]:
            passed.append(i)

    for i in reversed(passed):
        late_start_days.pop(i)
    
    if today == late_start_days[0]:
        await ctx.send("Today is a late start!")
    else:
        day_diff = late_start_days[0] - today
        await ctx.send("The next late start is in **" + str(day_diff.days) + "** days on **" + late_start_days[0].strftime("%b %d, %Y") + "**")

@client.command()
async def ls(ctx):
    today = date.today()

    passed = []
    
    if len(late_start_days) == 0:
        await ctx.send("There are no more late starts!")

    for i in range(len(late_start_days)):
        if today > late_start_days[i]:
            passed.append(i)

    for i in reversed(passed):
        late_start_days.pop(i)

    if today == late_start_days[0]:
        await ctx.send("Today is a late start!")
    else:
        day_diff = late_start_days[0] - today
        await ctx.send("The next late start is in **" + str(day_diff.days) + "** days on **" + late_start_days[0].strftime("%b %d, %Y") + "**")

@client.command()
async def help(ctx):
    help_embed = discord.Embed(colour=discord.Colour.blue(), title="Help", description="Mudkip Bot's Commands")
    
    help_embed.add_field(name="!genrandom", value="Generates a random number from 1-10", inline=False)
    help_embed.add_field(name="!genrandom start end", value="Generates a random number from start-end", inline=False)
    help_embed.add_field(name="!genrandom end", value="Generates a number from 1-end", inline=False)
    help_embed.add_field(name="!settimetable/!stt", value="Sets your timetable", inline=False)
    help_embed.add_field(name="!timetable/!tt", value="Sends your timetable", inline=False)
    help_embed.add_field(name="!day", value="Sends what day (1 or 2) it is today", inline=False)
    help_embed.add_field(name="!latestart/!ls", value="Sends when the next late start is", inline=False)

    await ctx.send(content=None, embed=help_embed)

client.run('MTAwNDU5Njk3OTMxOTQ0NzU5NA.Gx9iSP.7KRLo0QCF-rVC9p7_zhDac7lKERg0ed87yGOSo')
