import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
import database

load_dotenv()
my_secret = os.getenv('TOKEN')

client = discord.Client()

key_words = ['hearts', 'hoi4']
kr_key_words = ['kr', 'kaiser', 'kaiserreich', 'syndi', 'syndicalism']


# def add_roles(server, role):
#   if server.id in db.keys():
#     roles = db[server.id]
#     roles.append(role)
#     db[server.id] = roles
#   else:
#     db[server.id] = [role]


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


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(my_secret)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "$help":

        await message.channel.send("""
                                     Hello! I'm QuotBot\n\nI send quotes from players!\nIf you want quote - just type "hoi4" or "hearts"\n\nOther commands:\n\t$add "quote" - add a new quote\n\t$list - show list of quotes\n\t$delete_last - delete last added quote\n\t$last - recive last added quote\n\t$delete "index of quote" - delete added quote by index\n\nHave fun!\n\n
                                     """)

    elif message.content.lower().startswith("$add"):
        if check_roles(message):
            new_quote = message.content.split("$add ", 1)[1]
            database.update_quotes(new_quote)
            await message.channel.send("New quote added!")
        else:
            await message.channel.send("Not enough rights:c")
    #
    #
    elif message.content.lower().startswith("$list"):
        try:
            result = database.get_list()
            await message.channel.send(result)
        except database.EmptyError:
            await message.channel.send("There is none, please add some")

    elif message.content.lower() == "$last":
        try:
            result = database.get_last()
            await message.channel.send(result)
        except database.EmptyError:
            await message.channel.send("There is none, please add some")
    #
    elif message.content.lower().startswith("$delete_last"):
        if check_roles(message):
            try:
                database.delete_last_quote()
                await message.channel.send("Quote deleted!")
            except database.EmptyError:
                await message.channel.send("There is none, please add some")
        else:
            await message.channel.send("Not enough rights:c")

    elif message.content.lower().startswith("$delete"):
        if check_roles(message):
            index = int(message.content.split("$delete", 1)[1])
            try:
                database.delete_quote(index)
                await message.channel.send("Quote deleted!")
            except database.EmptyError:
                await message.channel.send("There is none, please add some")
        else:
            await message.channel.send("Not enough rights:c")


    else:
        if any(word in message.content.lower() for word in key_words):
            try:
                database.get_random_quote()
            except database.EmptyError:
                await message.channel.send("There is none, please add some")


keep_alive()
client.run(my_secret)
