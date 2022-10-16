import discord
from discord.ext import commands
import random


countrys_dict = {
    'UK': ['uk', 'united kingdom', 'britain', 'brits', 'england', 'brit', 'eng', 'en', '🇬🇧', 'churchill'],
    'USA': ['usa', 'us', 'america', 'murica', 'states', 'united states', 'united states of america', '🇺🇸', 'us of a', 'burger', '🍔', '🦅', 'fdr', '🌭'],
    'USA main': ['usa_main', 'usa main', '🇺🇸 main', 'us main', 'us_main'],
    'USA coop': ['usa_coop', 'usa coop', '🇺🇸 coop', 'us coop', 'us_coop'],
    'USSR': ['🇷🇺', 'sov', 'russia', 'soviet', 'ussr', 'stalin', 'gulag', 'vodka', '🐻', 'rus'],
    'USSR main': ['ussr_main', 'ussr main', 'sov main', '🇷🇺 main', 'sov_main'],
    'USSR coop': ['ussr_coop', 'ussr coop', 'sov coop', '🇷🇺 coop', 'sov_main'],
    'British Raj': ['🇮🇳', 'raj', 'india', 'british raj', 'ind', '🥻', '🐯'],
    'Canada': ['🇨🇦', 'can', 'canada', '🍁', '🦌', '🐺', '🦆'],
    'Australia': ['🇦🇺', 'australia', 'aus', 'ast', 'au', 'aussie', 'kangaroo', '🦘'],
    'South Africa': ['🇿🇦', 'saf', 'sa', 'south africa', 'africa', 'rsa', '🦁'],
    'New Zealand': ['🇳🇿', 'nz', 'new zealand', 'zealand', 'nzl', '🥝'],
    'Mexico': ['🇲🇽', 'mex', 'mexico', 'taco', '🌮'],
    'Brazil': ['🇧🇷', 'br', 'brazil', 'bra', 'brz', 'you are coming to brazil', '🐒'],
    'Mongolia': ['🇲🇳', 'mon', 'mongolia', '🐴'],
    'Germany': ['🇩🇪', 'ger', 'germany', 'hitler', 'wiener', 'beer', '🍺', 'deutschland'],
    'Germany main': ['germany_main', 'germany main', '🇩🇪 main', 'ger main', 'ger_main'],
    'Germany coop': ['germany_coop', 'germany coop', '🇩🇪 coop', 'ger coop', 'ger_coop'],
    'Italy': ['🇮🇹', 'mama mia', 'ita', 'italy', 'spaghetti', 'pizza', 'avanti', 'italia', 'mussolini', '🍝', '🍕'],
    'Japan': ['🇯🇵', 'anime', 'jp', 'japan', 'sushi', 'emperor', 'hirohito', 'jap', 'nippon', '🍣', '👘'],
    'Japan main': ['japan_main', 'japan main', '🇯🇵 main', 'jp main', 'jp_main'],
    'Japan coop': ['japan_coop', 'japan coop', '🇯🇵 coop', 'jp coop', 'jp_coop'],
    'Hungary': ['🇭🇺', 'hun', 'hungary', 'hungry', 'gulash', 'horthy', 'horny', 'magyar', "the hungry"],
    'Romania': ['🇷🇴', 'rom', 'romania', 'ganymania', 'judas'],
    'Bulgaria': ['🇧🇬', 'bul', 'bulgaria', 'bowlgaria', 'bulgreenia', 'boris'],
    'Spain': ['🇪🇸', 'spain', 'pain', 'spr', 'spa', 'franco'],
    'Finland': ['🇫🇮', 'fin', 'finland', 'perkele', 'niet molotov', '🐻‍❄️'],
    'Manchukuo': ['man', 'manchukuo', 'manchu', 'manchuria', 'puyi'],
    'Siam': ['🇹🇭', 'siam', 'thai', 'thailand', 'sia', '🐘']
}




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


def luck_choice(reserves):
    l = []
    for key, value in reserves.items():
        if value == '':
            l.append(key)
    return random.choice(l)
