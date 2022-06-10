import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select


flags_dict = {
    'UK': '🇬🇧',
    'USA': '🇺🇸',
    'France': '🇫🇷',
    'USSR': '🇷🇺',
    'China': '🇹🇼',
    'British Raj': '🇮🇳',
    'Canada': '🇨🇦',
    'Australia': '🇦🇺',
    'South Africa': '🇿🇦',
    'New Zealand': '🇳🇿',
    'Mexico': '🇲🇽',
    'Brazil': '🇧🇷',
    'Mongolia': '🇲🇳',
    'Germany': '🇩🇪',
    'Italy': '🇮🇹',
    'Japan': '🇯🇵',
    'Hungary': '🇭🇺',
    'Romania': '🇷🇴',
    'Bulgaria': '🇧🇬',
    'Spain': '🇪🇸',
    'Finland': '🇫🇮',
    'Vichy France': '🇹🇫',
    'Manchukuo': '🇳🇵',
    'Siam': '🇹🇭'
}






def check_reserves(reaction, user, reserves):
    for val in reserves.values():
        if str(user.name) in val:
            return False


    country = ''
    for key, value in flags_dict.items():
        if reaction.emoji == value:
            country = key     
            for key, value in reserves.items():
                if country in str(key) and value == '':
                    return True

    return False


def make_country_name(reaction, reserves):
    country = ''
    for key, value in flags_dict.items():
        if reaction.emoji == value:
            country = key     
            for key, value in reserves.items():
                if country in key and value == '':
                    return key




## TODO need proper emojis with proper IDs, and another dict with country names - IDs
