import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import os
from dotenv import load_dotenv
import database
import reservation as rsrv
import random

load_dotenv()
my_secret = os.getenv('TOKEN')
client = commands.Bot(command_prefix='$')
DiscordComponents(client)
key_words = ['hearts', 'hoi4']
reactions_list = []
open_reserve_flag = False
cute_names_list = ['bestie', 'cutie', 'sweety', 'puppy', 'kitten', 'gorgeous']


def check_roles(msg):
    try:
        author_roles = msg.author.roles
        access_roles = ['tester1', 'tester2', 'Field Marshal', 'Moderator']
        for role in author_roles:
            if role.name in access_roles:
                return True
        return False
    except AttributeError:
        return False


def check_reservations_channel(msg):
    chl = str(msg.channel)
    if chl in ['reservationstest', 'reservations']:
        print(chl)
        return True
    return False


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


@client.command()
async def bothelp(ctx):
    message = """I send quotes from players!\n
    If you want quote - just type "hoi4" or "hearts"\n\n
    Other commands:\n
    $add "quote" - add a new quote\n
    $botlist - show list of quotes\n
    $delete_last - delete last added quote\n
    $last - recive last added quote\n
    $delete "index of quote" - delete added quote by index\n\n
    Have fun!\n\n"""

    embed = discord.Embed(
        title="Hello! I'm QuotBot!",
        description=message,
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)


@client.command()
async def add(ctx):
    if check_roles(ctx):
        new_quote = ctx.message.content.split("$add ", 1)[1]
        database.update_quotes(new_quote)
        await ctx.send("New quote added!")
    else:
        await ctx.send("Not enough rights:c")


@client.command()
async def delete_last(ctx):
    if check_roles(ctx):
        try:
            database.delete_last_quote()
            await ctx.send("Quote deleted!")
        except database.EmptyError:
            await ctx.send("There is none, please add some")
    else:
        await ctx.send("Not enough rights:c")


@client.command()
async def botlist(ctx):
    try:
        result = database.get_list()
        await ctx.send(result)
    except database.EmptyError:
        await ctx.send("There is none, please add some")


@client.command()
async def last(ctx):
    try:
        result = database.get_last()
        await ctx.send(result)
    except database.EmptyError:
        await ctx.send("There is none, please add some")


@client.command()
async def delete(ctx, arg):
    if check_roles(ctx):
        index = int(arg)
        try:
            database.delete_quote(index)
            await ctx.send("Quote deleted!")
        except database.EmptyError:
            await ctx.send("There is none, please add some")
    else:
        await ctx.send("Not enough rights:c")


@client.event
async def on_message(message):
    if any(word in message.content.lower() for word in key_words):
        print(message.content.lower())
        try:
            result = database.get_random_quote()
            await message.channel.send(result)
        except database.EmptyError:
            await message.channel.send("There is none, please add some")
    await client.process_commands(message)


@client.command()
async def help_res(ctx):
    if check_reservations_channel(ctx):
        msg = """
        Field Marshals and Moderators can open and close reservation process by using commands:\n
        👉 $reserv_open - Reservations are open! Everyone is free to reserv\n
        👉 $reserv_close - Reservations are closed💀\n\n
        Other commands can be used by everyone!\n
        👉 $res country_name - Reserv the country!\n
        👉 $cancel - Cancel your reservation!\n
        👉 $status - Display the current status of reservations\n 
        Have fun!
        Alex production :3
        """
        embed = discord.Embed(
            title="Alright, here's the THING",
            description=msg,
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
    else:
        msg = """Sorry, works only in Reservation channel"""
        embed = discord.Embed(
            title=msg,
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


@client.command()
async def reserv_open(ctx):
    if check_reservations_channel(ctx) and check_roles(ctx):
        database.open_res()
        msg = 'Here we go! Please use command "$res country_name" to reserv country you wanna play, for example "$res germany"!'

        reserves = database.get_res()
        reserves_result = '\n'.join(
            ' - '.join((key, val)) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=reserves_result
        )
        await ctx.send(embed=embed)

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)}")
    elif not check_roles(cts):
        await ctx.send(f"Not enough rights {random.choice(cute_names_list)} =() ")


@client.command()
async def res(ctx):
    if check_reservations_channel(ctx) and database.get_flag():
        msg = ctx.message.content.split("$res ", 1)[1]
        if rsrv.country_check(msg):
            user = str(ctx.message.author.name)
            reserves = database.get_res()
            country = rsrv.make_country_name(msg, reserves)
            if rsrv.check_reserves_empty(msg, user, reserves):
                database.update_res(user, country)
                await ctx.send(f'{user} reserved {country}')
            else:
                await ctx.send(f"Prolly country already reserved, or you already have reservation, {random.choice(cute_names_list)}. Check $status")
        else:
            await ctx.send(f"Prolly you misspelled country name, {random.choice(cute_names_list)}, try again 😉")

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)}")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)}")


@client.command()
async def cancel(ctx):
    if check_reservations_channel(ctx) and database.get_flag():

        user = str(ctx.message.author.name)
        reserves = database.get_res()
        if rsrv.check_unreserve(user, reserves):
            country = database.get_country_by_user(user)
            database.remove_res(user)

            await ctx.send(f'{user} UNreserved {country}')
        else:
            await ctx.send(f"Prolly you didn't reserve anything, {random.choice(cute_names_list)}")

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)}")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)}")


@client.command()
async def status(ctx):
    if check_reservations_channel(ctx) and database.get_flag():
        msg = 'Status of the Game'

        reserves = database.get_res()
        reserves_result = '\n'.join(
            ' - '.join((key, val)) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=reserves_result
        )

        await ctx.send(embed=embed)

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)}")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)}")


@client.command()
async def reserv_close(ctx):
    if check_reservations_channel(ctx) and check_roles(ctx) and database.get_flag():
        msg = 'Reservations are closed! Here is final status of the Game'

        reserves = database.get_res()
        reserves_result = '\n'.join(
            ' - '.join((key, val)) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=reserves_result
        )

        await ctx.send(embed=embed)
        database.close_res()

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)}")

    elif not check_roles(cts):
        await ctx.send(f"Not enough rights {random.choice(cute_names_list)} =(")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)}")


client.run(my_secret)
