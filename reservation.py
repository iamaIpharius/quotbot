import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select


countrys_dict = {
    'UK': ['uk', 'united kingdom', 'britain', 'brits', 'england', 'brit', 'eng', 'en', '🇬🇧'],
    'USA': ['usa', 'us', 'america', 'murica', 'states', 'united states', 'united states of america', '🇺🇸'],
    'France': ['🇫🇷', 'fr', 'france', 'fronce'],
    'USSR': ['🇷🇺', 'sov', 'russia', 'soviet', 'ussr', 'stalin', 'gulag', 'vodka'],
    'China': ['🇹🇼', 'china', 'chi', 'chang'],
    'British Raj': ['🇮🇳', 'raj', 'india', 'british raj'],
    'Canada': ['🇨🇦', 'can', 'canada'],
    'Australia': ['🇦🇺', 'australia', 'aus', 'au', 'aussie', 'kangooroo'],
    'South Africa': ['🇿🇦', 'saf', 'sa', 'south africa', 'africa'],
    'New Zealand': ['🇳🇿', 'nz', 'new zealand', 'zealand'],
    'Mexico': ['🇲🇽', 'mex', 'mexico', 'taco'],
    'Brazil': ['🇧🇷', 'br', 'brazil'],
    'Mongolia': ['🇲🇳', 'mon', 'mongolia'],
    'Germany': ['🇩🇪', 'ger', 'germany', 'hitler', 'wiener', 'beer'],
    'Italy': ['🇮🇹', 'mama mia', 'ita', 'italy', 'spaghetti', 'pizza'],
    'Japan': ['🇯🇵', 'anime', 'jp', 'japan', 'sushi', 'emperor', 'ninja', 'hentai'],
    'Hungary': ['🇭🇺', 'hun', 'hungary', 'hungry', 'gulas', 'horti', 'horny'],
    'Romania': ['🇷🇴', 'rom', 'romania', 'ganymania'],
    'Bulgaria': ['🇧🇬', 'bul', 'bulgaria', 'bowlgaria', 'bulgreenia'],
    'Spain': ['🇪🇸', 'spain', 'pain'],
    'Finland': ['🇫🇮', 'fin', 'finland', 'perkele', 'niet molotov'],
    'Vichy France': ['vichy', 'vichy france'],
    'Manchukuo': ['man', 'manchukuo', 'manchu', 'manchuria'],
    'Siam': ['🇹🇭', 'siam', 'thai', 'thailand']
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
    for key, value in countrys_dict.items():
        if message.lower() in value:
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
    for key, value in countrys_dict.items():
        if message.lower() in value:
            country = key
            for key, value in reserves.items():
                if country in key and value == '':
                    return key


def country_check(m):
    for countries in countrys_dict.values():
        if m.lower() in countries:
            return True
    return False
