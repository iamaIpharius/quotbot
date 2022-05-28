import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import os
from dotenv import load_dotenv
import database
import reservation as rsrv

load_dotenv()
my_secret = os.getenv('TOKEN')
client = commands.Bot(command_prefix='$')
DiscordComponents(client)
key_words = ['hearts', 'hoi4']
buttons_list = ['usa_button', 'ger_button', 'uk_button']
open_reserve_flag = False


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
async def helpreserv(ctx):
    if check_reservations_channel(ctx):
        msg = """Here will be help stuff for reservations"""
        embed = discord.Embed(
            title=msg,
            description='SOONish...',
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
    if check_reservations_channel(ctx):
        database.open_res()
        open_reserve_flag = True
        msg = 'Here we go! Please choose the country you wanna play'
        embed = discord.Embed(
            title=msg,
            color=discord.Color.green()
        )
        main_components = rsrv.start_components
        await ctx.send(embed=embed, components=main_components)
        while open_reserve_flag:
            # try:
            interaction = await client.wait_for("button_click", check=lambda i: i.custom_id in buttons_list)
            database.update_res(str(interaction.author), str(interaction.component.label))
            reserves = database.get_res()
            print(reserves)
            reserves_result = '\n'.join(' - '.join((key, val)) for (key, val) in reserves.items())

            print(reserves_result)

            embed = discord.Embed(
                title=msg,
                color=discord.Color.green(),
                description=reserves_result
            )
            await interaction.message.edit(embed=embed)
            await interaction.send(f'{interaction.author} reserved {interaction.component.label}')
            # except:
            #     await ctx.send('error')


client.run(my_secret)
