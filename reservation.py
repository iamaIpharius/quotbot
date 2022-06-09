import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select


def check_reserves(reaction, user, reserves):
    for val in reserves.values():
        if str(user) in val:

            return False
    for key, value in reserves.items():
        if str(reaction.emoji) in str(key) and value == '':
            return True

    return False


def make_country_name(reaction, reserves):
    for key, value in reserves.items():
        if str(reaction.emoji) in key and value == '':
            return key




## TODO need proper emojis with proper IDs, and another dict with country names - IDs
