import discord
from discord.ext import commands

import random


countrys_dict_hist = {
    'UK': ['uk', 'united kingdom', 'britain', 'brits', 'england', 'brit', 'eng', 'en', '🇬🇧', 'churchill'],
    'USA': ['usa', 'us', 'america', 'murica', 'states', 'united states', 'united states of america', '🇺🇸', 'us of a', 'burger', '🍔', '🦅', 'fdr', '🌭'],
    'USA main': ['usa_main', 'usa main', '🇺🇸 main', 'us main', 'us_main'],
    'USA coop': ['usa_coop', 'usa coop', '🇺🇸 coop', 'us coop', 'us_coop'],
    'USSR': ['🇷🇺', 'sov', 'russia', 'soviet', 'ussr', 'stalin', 'gulag', 'vodka', '🐻', 'rus'],
    'USSR main': ['ussr_main', 'ussr main', 'sov main', '🇷🇺 main', 'sov_main'],
    'USSR coop': ['ussr_coop', 'ussr coop', 'sov coop', '🇷🇺 coop', 'sov_coop'],
    'British Raj': ['🇮🇳', 'raj', 'india', 'british raj', 'ind', '🥻', '🐯'],
    'Canada': ['🇨🇦', 'can', 'canada', '🍁', '🦌', '🐺', '🦆'],
    'Australia': ['🇦🇺', 'australia', 'aus', 'ast', 'au', 'aussie', 'kangaroo', '🦘'],
    'South Africa': ['🇿🇦', 'saf', 'sa', 'south africa', 'africa', 'rsa', '🦁'],
    'New Zealand': ['🇳🇿', 'nz', 'new zealand', 'zealand', 'nzl', '🥝'],
    'Mexico': ['🇲🇽', 'mex', 'mexico', 'taco', '🌮'],
    'Mongolia': ['🇲🇳', 'mon', 'mongolia', '🐴'],
    'Germany': ['🇩🇪', 'ger', 'germany', 'hitler', 'wiener', 'beer', '🍺', 'deutschland'],
    'Germany main': ['germany_main', 'germany main', '🇩🇪 main', 'ger main', 'ger_main'],
    'Germany coop': ['germany_coop', 'germany coop', '🇩🇪 coop', 'ger coop', 'ger_coop'],
    'Italy': ['🇮🇹', 'mama mia', 'ita', 'italy', 'spaghetti', 'pizza', 'avanti', 'italia', 'mussolini', '🍝', '🍕'],
    'Japan': ['🇯🇵', 'anime', 'jp', 'japan', 'sushi', 'emperor', 'hirohito', 'jap', 'nippon', '🍣', '👘'],
    'Japan main': ['japan_main', 'japan main', '🇯🇵 main', 'jp main', 'jp_main'],
    'Japan coop': ['japan_coop', 'japan coop', '🇯🇵 coop', 'jp coop', 'jp_coop'],
    'Hungary': ['🇭🇺', 'hun', 'hungary', 'hungry', 'gulash', 'horthy', 'horny', 'magyar', 'the hunger'],
    'Romania': ['🇷🇴', 'rom', 'romania', 'ganymania', 'judas'],
    'Bulgaria': ['🇧🇬', 'bul', 'bulgaria', 'bowlgaria', 'bulgreenia', 'boris'],
    'Spain': ['🇪🇸', 'spain', 'pain', 'spr', 'spa', 'franco'],
    'Finland': ['🇫🇮', 'fin', 'finland', 'perkele', 'niet molotov', '🐻‍❄️'],
    'Manchukuo': ['man', 'manchukuo', 'manchu', 'manchuria', 'puyi'],
    'Siam': ['🇹🇭', 'siam', 'thai', 'thailand', 'sia', '🐘'],
    'Vichy': ['vichy', 'petain', 'traitors', 'vic', 'vich']
}

countrys_dict_pony = {
    'EQUESTRIA': ['eqs','equ', 'equestria', 'pony', '🦄', 'celestia'],
    'EQUESTRIA MAIN': ['equ main','eqs main', 'equestria main','pony', '🦄', 'celestia'],
    'EQUESTRIA COOP': ['equ coop','eqs coop', 'equestria coop','pony', '🦄', 'celestia'],
    'CRYSTAL EMPIRE': ['cry', 'crystal','🍁'],
    'NEW MARELAND': ['eqc','mar', 'mareland','🦘'],
    'STALLIONGRAD': ['stg','sta', 'stalin', 'stalliongrad', 'grad','🐯'],
    'CHANGELING LANDS': ['chn','cha', 'change', 'changelings','changeling', 'lands','🪲','🇩🇪', '🍺'],
    'CHANGELING LANDS MAIN': ['chn main','cha main', 'change main', 'lands main','🪲','🇩🇪', '🍺'],
    'CHANGELING LANDS COOP': ['chn coop','cha coop', 'change coop', 'lands coop','🪲','🇩🇪', '🍺'],
    'CHANGELING LANDS COOP #2': ['chn coop','cha coop', 'change coop', 'lands coop','🪲','🇩🇪', '🍺'],
    'WINGBARDY': ['wng','win', 'wingbardy','🇮🇹', 'mama mia','spaghetti','pizza','🍝', '🍕'],
    'GRENECLYF': ['gre', 'greneclyf'],
    'OLENIA': ['ole', 'olenia', 'deer', '🏳️‍🌈', '🦌'],
    'POLAR BEARS': ['plb','pol', 'polar', 'bears','🐻‍❄️', 'polar bears', 'polar bear'],
    'HIPPOGRIFFIA': ['hip','hip main', 'hippogriffia', ':posadaChamp:'],
    'HIPPOGRIFFIA COOP': ['hip','hip coop', 'hippogriffia', ':posadaChamp:'],
    'COLTHAGE': ['cth','col','colthage', 'hannibal', '🐘'],
    'CHIROPTERRA': ['bat','chi', 'chiropterra', '🦇'],
    'BUFFALO KINGDOM': ['buf', 'buffalo', 'gorick', 'crake', '🦬'],
    'WARZENA KINGDOM': ['war', 'warzena', 'zena','🦓']
}


def check_reserves_empty(message, user, reserves, countrys_dict):
    for val in reserves.values():
        if user == val:
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


def make_country_name(message, reserves, countrys_dict):
    country = ''
    for key, value in countrys_dict.items():
        if message.lower() in value:
            country = key
            for key, value in reserves.items():
                if country in key and value == '':
                    return key


def country_check(m, countrys_dict):
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
