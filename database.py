from tinydb import TinyDB, Query
import random
import json

db = TinyDB('db.json')

Cursor = Query()


class EmptyError(BaseException):
    def __init__(self):
        pass


reserv_template = {
    'UK': '',
    'USA main': '',
    'USA coop': '',
    'France': '',
    'USSR main': '',
    'USSR coop': '',
    'China': '',
    'British Raj': '',
    'Canada': '',
    'Australia': '',
    'South Africa': '',
    'New Zealand': '',
    'Mexico': '',
    'Brazil': '',
    'Mongolia': '',
    'Germany main': '',
    'Germany coop': '',
    'Italy': '',
    'Japan main': '',
    'Japan coop': '',
    'Hungary': '',
    'Romania': '',
    'Bulgaria': '',
    'Spain': '',
    'Finland': '',
    'Vichy France': '',
    'Manchukuo': '',
    'Siam': ''
}


# reserv_template = {
#     'UK :flag_gb:': '',
#     'USA main :flag_us:': '',
#     'USA coop :flag_us:': '',
#     'France :flag_fr:': '',
#     'USSR main 🇷🇺': '',
#     'USSR coop 🇷🇺': '',
#     'China 🇹🇼': '',
#     'British Raj 🇮🇳': '',
#     'Canada 🇨🇦': '',
#     'Australia 🇦🇺': '',
#     'South Africa 🇿🇦': '',
#     'New Zealand 🇳🇿': '',
#     'Mexico 🇲🇽': '',
#     'Brazil 🇧🇷': '',
#     'Mongolia 🇲🇳': '',
#     'Germany main 🇩🇪': '',
#     'Germany coop 🇩🇪': '',
#     'Italy 🇮🇹': '',
#     'Japan main 🇯🇵': '',
#     'Japan coop 🇯🇵': '',
#     'Hungary 🇭🇺': '',
#     'Romania 🇷🇴': '',
#     'Bulgaria 🇧🇬': '',
#     'Spain 🇪🇸': '',
#     'Finland 🇫🇮': '',
#     'Vichy France 🇹🇫': '',
#     'Manchukuo 🇳🇵': '',
#     'Siam 🇹🇭': ''
# }


def update_quotes(quote):
    if db.get(Cursor.name == "player_quotes"):
        dict_quotes = db.get(Cursor.name == "player_quotes")
        print(dict_quotes)
        base = dict_quotes['content']
        base.append(quote)
        print(base)
        db.update({'content': base}, Cursor.name == "player_quotes")
    else:
        db.insert({'name': 'player_quotes', 'content': [quote]})


def delete_last_quote():
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        base = base[:-1]
        db.update({'content': base}, Cursor.name == "player_quotes")
        return
    else:
        raise EmptyError


def delete_quote(index):
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        if len(base) >= index - 1:
            index_element = base.pop(index - 1)
            db.update({'content': base}, Cursor.name == "player_quotes")
        return
    else:
        raise EmptyError


def get_random_quote():
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        random_quote = random.choice(base)
        return random_quote
    else:
        raise EmptyError


def get_list():
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        result_string = ''
        for index, q in enumerate(base, 1):
            result_string = result_string + f"{index}. {q}\n"
        return result_string
    else:
        raise EmptyError


def get_last():
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        last_quote = base[-1]
        return last_quote
    else:
        raise EmptyError


def open_res():
    if db.get(Cursor.name == "reservations"):
        db.update({'content': reserv_template, 'flag': True},
                  Cursor.name == "reservations")
    else:
        db.insert({'name': 'reservations',
                   'content': reserv_template, 'flag': True})


def update_res(user, country):
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        base[country] = user
        db.update({'content': base}, Cursor.name == "reservations")
    else:
        db.insert({'name': 'reservations', 'content': {country: user}})


def remove_res(user):
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        for key, value in base.items():
            if user == value:
                base[key] = ''

        db.update({'content': base}, Cursor.name == "reservations")


def get_res():
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        return base


def close_res():
    if db.get(Cursor.name == "reservations"):
        db.update({'content': reserv_template, 'flag': False},
                  Cursor.name == "reservations")
    else:
        db.insert({'name': 'reservations',
                   'content': reserv_template, 'flag': False})


def get_flag():
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['flag']
        return base


def get_country_by_user(user):
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        for key, value in base.items():
            if user == value:
                return str(key)
