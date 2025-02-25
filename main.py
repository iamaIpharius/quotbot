import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
import database
import reservation as rsrv
import random
import glitch as gl

load_dotenv()
my_secret = os.getenv('TOKEN')
client = commands.Bot(command_prefix='$', help_command=None)

key_words = ['hearts', 'hoi4']
cute_names_list = ['bestie', 'cutie', 'sweety', 'puppy', 'kitten', 'gorgeous', 'cutie pie',
                   'sunshine', 'sweetheart', 'muffin', 'sweetheart', 'sweet pea', 'cutie patootie']

lucky_choice_emotes = ['✨', '🌟', '🔥', '🥳', '🍀', '☘️', '😂', '😹', "😊",
                       '😎', '🦄', '🍭', '🎈', '🎢', '🎡', '⚡', '🧙', '🎇', '🎆', '💎', '🌠', '😀', '🌞']


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
        return True
    return False


def check_bot_channel(msg):
    chl = str(msg.channel)
    if chl in ['funbot']:
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
async def help(ctx):
    if check_reservations_channel(ctx):
        msg = """### Below you can see **Reservations rules** and **Commands** to use bot 🤖\n\n
        🗒️ Nations can be reserved by their name, their flag, and their tag\n
        🗒️ To reserve directly coop or main please use nation name, flag or tag with coop or main (i.e. $ger coop)\n\n
        **Field Marshals and Moderators can open and close reservation process by using commands:**\n
        👉 $res_open - Reservations are open! Everyone is free to reserve\n
        👉 $res_close - Reservations are closed 💀\n\n
        **Other commands can be used by everyone!**\n
        👉 $res country_name - Reserve the country!\n
        👉 $cancel - Cancel your reservation!\n
        👉 $status - Display the current status of reservations\n
        👉 $luck - .......TRY YOUR LUCK (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n
        Have fun!\n\n\n
        🐴🐴🐴🐴🐴 **BOT SUPPORTS PONY MOD** 🐴🐴🐴🐴🐴\n\n
        🦄 PONYNATIONS can be reserverd by their tag (3 firts letters)\n
        🦄 To reserve directly coop or main please tag with coop or main (i.e. $equ coop)\n\n
        **Field Marshals and Moderators can open and close reservation process by using commands:**\n
        🐎 $res_open_pony - Reservations are open! Everyone is free to reserve\n
        🐎 $res_close_pony - Reservations are closed 💀\n\n
        **Other commands can be used by everyone!**\n
        🐎 $res_pony country_name - Reserve the country!\n
        🐎 $cancel_pony - Cancel your reservation!\n
        🐎 $status_pony - Display the current status of reservations\n\n
        Reservations rules:\n
        🖋️ This script applies to Historical games.\n
        🖋️ If you reserve a nation please be willing and able to show up on time on game day.\n
        🖋️ If you reserve a nation and do not show you may lose the ability to reserve a nation in the future for an amount of time\n
        🖋️ If you are reserving a Major please be capable of playing said nation, or have an experienced co-op to guide you. If you are unsure please ask the staff.\n
        🖋️ The faction leaders may decide on their choice of minors at game start, this will override any reservations made.\n
        🖋️ If you reserve a nation two games in a row your reservation may be superseded by someone else. Exemptions can be made by staff.\n
        🖋️ Staff reserve the right to move players off their reservations (Major or Minor) at start time to balance the game.\n
        """
        embed = discord.Embed(
            title="Alright, here's the THING",
            description=msg,
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
    else:
        message = """I can send quotes from players and manage reservations!\n
        If you want quote - just type "hoi4" or "hearts"\n\n
        Other commands:\n
        ( ͡° ͜ʖ ͡°) $add "quote" - add a new quote\n
        ( ͡° ͜ʖ ͡°) $list - show list of quotes\n
        ( ͡° ͜ʖ ͡°) $delete_last - delete last added quote\n
        ( ͡° ͜ʖ ͡°) $last - recive last added quote\n
        ( ͡° ͜ʖ ͡°) $delete "index of quote" - delete added quote by index\n\n
        Have fun!\n\n
        You can check reservation rules by typing $help command in #reservations channel!\n
        """

        embed = discord.Embed(
            title=f"Hello! I'm {client.user.name}! 🤖",
            description=message,
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)


@client.command()
async def add(ctx):
    if check_roles(ctx):
        new_quote = ctx.message.content.split("$add ", 1)[1]
        database.update_quotes(new_quote)
        await ctx.send("New quote added! **( ͡° ͜ʖ ͡°)**")
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
async def list(ctx):
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
    if message.author == client.user:
        return
    elif any(word in message.content.lower() for word in key_words) and not message.content.lower().startswith('$'):
        try:
            result = database.get_random_quote()
            await message.channel.send(result)
        except database.EmptyError:
            await message.channel.send("There is none, please add some")
    await client.process_commands(message)
    if check_bot_channel(message):
        if message.author == client.user:
            return
        if message.attachments:
            print(message.attachments)
            img_url = message.attachments[0].url
            level = 5
            if type(message.content) == int and 0 < message.content <= 10:
                level = message.content
            final_image = gl.do_glitch(img_url, level)
            await message.channel.send('Here you are!', file=final_image)


@client.command()
async def res_open(ctx):
    if check_reservations_channel(ctx) and check_roles(ctx):
        database.open_res()
        msg = "Here we go! (☞ﾟ∀ﾟ)☞\nPlease use command $res to reserve country that you wanna play!\n"

        reserves, count = database.get_res()
        reserves_message_head = """
        🖋️ Nations can be reserved by their name, their flag, and their tag\n
        🖋️ To reserve directly coop or main please use nation name, flag or tag with coop or main (i.e. $ger coop)

        """
        reserves_result = '\n'.join(
            ' - '.join((key, val)) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=reserves_message_head + reserves_result
        )
        await ctx.send(embed=embed)

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)} ¯\_(ツ)_/¯")
    elif not check_roles(ctx):
        await ctx.send(f"Not enough rights {random.choice(cute_names_list)} :c")

@client.command()
async def res_open_pony(ctx):
    if check_reservations_channel(ctx) and check_roles(ctx):
        database.open_res_pony()
        msg = "🐎🐎🐎 Here we go! 🐎🐎🐎\nPlease use command $res_pony to reserve **PONYMOD NATION** that you wanna play!"


        reserves, count = database.get_res_pony()
        reserves_message_head = """
        🖋️ Nations can be reserved by their name or tag (first 3 letters) EXAMPLE: $res_pony pol\n
        🖋️ To reserve directly coop or main please use nation name, tag (first 3 letters) with coop or main (i.e. $equ coop)

        """
        reserves_result = '\n'.join(
            ' - '.join((key, val)) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=reserves_message_head + reserves_result
        )
        await ctx.send(embed=embed)

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)} ¯\_(ツ)_/¯")
    elif not check_roles(ctx):
        await ctx.send(f"Not enough rights {random.choice(cute_names_list)} :c")

@client.command()
async def res(ctx):
    if check_reservations_channel(ctx) and database.get_flag():
        msg = ctx.message.content.split("$res ", 1)[1]
        if msg == 'cancel':
            user = ctx.message.author.display_name
            user_mention = ctx.message.author.mention
            reserves, count = database.get_res()
            if rsrv.check_unreserve(user, reserves):
                country = database.get_country_by_user(user)
                database.remove_res(user)

                await ctx.send(f'{user_mention} unreserved **{country}** 🏳️')
            else:
                await ctx.send(f"Prolly you didn't reserve anything, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")
        elif rsrv.country_check(msg, rsrv.countrys_dict_hist):
            user = ctx.message.author.display_name
            user_mention = ctx.message.author.mention
            reserves, count = database.get_res()
            country = rsrv.make_country_name(msg, reserves, rsrv.countrys_dict_hist)
            if rsrv.check_reserves_empty(msg, user, reserves, rsrv.countrys_dict_hist):
                database.update_res(user, country)
                await ctx.send(f'{user_mention} reserved **{country}**!')
            else:
                await ctx.send(
                    f"Prolly country already reserved, or you already have reservation, {random.choice(cute_names_list)} ¯\_(ツ)_/¯. Check $status 😉")
        elif msg in ['bhutan']:
            await ctx.send(f"Hey {random.choice(cute_names_list)}, BHUTAN is FORBIDDEN 😠")

        else:
            await ctx.send(f"Prolly you misspelled country name, {random.choice(cute_names_list)}, try again 😉")

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def res_pony(ctx):
    if check_reservations_channel(ctx) and database.get_flag_pony():
        msg = ctx.message.content.split("$res_pony ", 1)[1]
        if msg == 'cancel':
            user = ctx.message.author.display_name
            user_mention = ctx.message.author.mention
            reserves, count = database.get_res_pony()
            if rsrv.check_unreserve(user, reserves):
                country = database.get_country_by_user_pony(user)
                database.remove_res_pony(user)

                await ctx.send(f'{user_mention} unreserved **{country}** 🏳️')
            else:
                await ctx.send(f"Prolly you didn't reserve anything, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")
        elif rsrv.country_check(msg, rsrv.countrys_dict_pony):
            user = ctx.message.author.display_name
            user_mention = ctx.message.author.mention
            reserves, count = database.get_res_pony()
            country = rsrv.make_country_name(msg, reserves, rsrv.countrys_dict_pony)
            if rsrv.check_reserves_empty(msg, user, reserves, rsrv.countrys_dict_pony):
                database.update_res_pony(user, country)
                await ctx.send(f'{user_mention} reserved **{country}**!')
            else:
                await ctx.send(
                    f"Prolly country already reserved, or you already have reservation, {random.choice(cute_names_list)} ¯\_(ツ)_/¯. Check $status 😉")

        else:
            await ctx.send(f"Prolly you misspelled country name, {random.choice(cute_names_list)}, try again 😉")

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def cancel(ctx):
    if check_reservations_channel(ctx) and database.get_flag():

        user = ctx.message.author.display_name
        user_mention = ctx.message.author.mention
        reserves, count = database.get_res()
        if rsrv.check_unreserve(user, reserves):
            country = database.get_country_by_user(user)
            database.remove_res(user)

            await ctx.send(f'{user_mention} unreserved **{country}** 🏳️')
        else:
            await ctx.send(f"Prolly you didn't reserve anything, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def cancel_pony(ctx):
    if check_reservations_channel(ctx) and database.get_flag_pony():

        user = ctx.message.author.display_name
        user_mention = ctx.message.author.mention
        reserves, count = database.get_res_pony()
        if rsrv.check_unreserve(user, reserves):
            country = database.get_country_by_user_pony(user)
            database.remove_res_pony(user)

            await ctx.send(f'{user_mention} unreserved **{country}** 🏳️')
        else:
            await ctx.send(f"Prolly you didn't reserve anything, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def status(ctx):
    if check_reservations_channel(ctx) and database.get_flag():
        msg = 'Status of the Game (ﾉ◕ヮ◕)ﾉ:･ﾟ✧ ✧ﾟ･: ヽ(◕ヮ◕ヽ)'

        reserves, count = database.get_res()
        total_players_string = f"""\n```fix\nTotal players: {count}```\n"""
        reserves_result = '\n'.join(
            ' - '.join((key, val if len(val) < 2 else f"**{val}**")) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=total_players_string + reserves_result
        )

        await ctx.send(embed=embed)

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def status_pony(ctx):
    if check_reservations_channel(ctx) and database.get_flag_pony():
        msg = '🐎🐎🐎 Status of the Game 🐎🐎🐎'

        reserves, count = database.get_res_pony()
        total_players_string = f"""\n```fix\nTotal players: {count}```\n"""
        reserves_result = '\n'.join(
            ' - '.join((key, val if len(val) < 2 else f"**{val}**")) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=total_players_string + reserves_result
        )

        await ctx.send(embed=embed)

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def res_close(ctx):
    if check_reservations_channel(ctx) and check_roles(ctx) and database.get_flag():

        msg = f"Reservations are closed!"

        reserves, count = database.get_res()
        total_players_string = f"""\n```fix\nTotal players: {count}```\n"""
        reserves_result = '\n'.join(
            ' - '.join((key, val if len(val) < 2 else f"**{val}**")) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=total_players_string + reserves_result
        )

        await ctx.send(embed=embed)
        database.close_res()


    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    elif not check_roles(ctx):
        await ctx.send(f"Not enough rights, {random.choice(cute_names_list)} :c")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def res_close_pony(ctx):
    if check_reservations_channel(ctx) and check_roles(ctx) and database.get_flag_pony():

        msg = f"🐎🐎🐎Reservations are closed!🐎🐎🐎"

        reserves, count = database.get_res_pony()
        total_players_string = f"""\n```fix\nTotal players: {count}```\n"""
        reserves_result = '\n'.join(
            ' - '.join((key, val if len(val) < 2 else f"**{val}**")) for (key, val) in reserves.items())

        embed = discord.Embed(
            title=msg,
            color=discord.Color.green(),
            description=total_players_string + reserves_result
        )

        await ctx.send(embed=embed)
        database.close_res()


    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    elif not check_roles(ctx):
        await ctx.send(f"Not enough rights, {random.choice(cute_names_list)} :c")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

@client.command()
async def luck(ctx):
    if check_reservations_channel(ctx) and database.get_flag():

        user = ctx.message.author.display_name
        user_mention = ctx.message.author.mention
        reserves, count = database.get_res()
        if not rsrv.check_unreserve(user, reserves):
            country = rsrv.luck_choice(reserves)
            database.update_res(user, country)
            lucky_str = ''.join(
                [random.choice(lucky_choice_emotes) for _ in range(3)])
            lucky_str = lucky_str + lucky_str[1] + lucky_str[0]
            await ctx.send(f'Lucky choice for {user_mention} is **{country}** {lucky_str}')
        else:
            database.remove_res(user)
            reserves, count = database.get_res()
            country = rsrv.luck_choice(reserves)
            database.update_res(user, country)
            lucky_str = ''.join(
                [random.choice(lucky_choice_emotes) for _ in range(3)])
            lucky_str = lucky_str + lucky_str[1] + lucky_str[0]
            await ctx.send(f'Lucky choice for {user_mention} is **{country}** {lucky_str}')

    elif not check_reservations_channel(ctx):
        await ctx.send(f"Wrong channel {random.choice(cute_names_list)} ¯\_(ツ)_/¯")

    else:
        await ctx.send(f"Reservations aren't open yet, {random.choice(cute_names_list)} ¯\_(ツ)_/¯")



client.run(my_secret)
