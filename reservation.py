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

country_list = [
    'UK',
    'USA main',
    'USA coop',
    'France',
    'USSR main',
    'USSR coop',
    'China',
    'British Raj',
    'Canada',
    'Australia',
    'South Africa',
    'New Zealand',
    'Mexico',
    'Brazil',
    'Mongolia',
    'Germany main',
    'Germany coop',
    'Italy',
    'Japan main',
    'Japan coop',
    'Hungary',
    'Romania',
    'Bulgaria',
    'Spain',
    'Finland',
    'Vichy France',
    'Manchukuo',
    'Siam']


def check_reserves_empty(message, user, reserves):
    for val in reserves.values():
        if user in val:
            return False

    country = ''
    for key, value in flags_dict.items():
        if message.lower() in key.lower():
            country = key
            for key, value in reserves.items():
                if country in str(key) and value == '':
                    return True

    return False


def check_unreserve(user, reserves):
    if user in reserves.values():
        return True
    return False


def make_country_name(message, reserves):
    country = ''
    for key, value in flags_dict.items():
        if message.lower() in key.lower():
            country = key
            for key, value in reserves.items():
                if country in key and value == '':
                    return key


def country_check(m):
    country_list = ['uk', 'usa main', 'usa coop', 'france', 'ussr main', 'ussr coop',
                    'china', 'british raj', 'canada', 'australia',
                    'south africa', 'new zealand', 'mexico', 'brazil',
                    'mongolia', 'germany main', 'germany coop', 'italy',
                    'japan main', 'japan coop', 'hungary', 'romania',
                    'bulgaria', 'spain', 'finland', 'vichy france', 'manchukuo', 'siam']
    for country in country_list:
        if m.lower() in country:
            return True
    return False
