from tinydb import TinyDB, Query
import random
import json

db = TinyDB('db.json')

Cursor = Query()


class EmptyError(BaseException): #simple exeption
    def __init__(self):
        pass


reserv_template = { #template for reservation messages
    'UK': '',
    'USA main': '',
    'USA coop': '',
    'USSR main': '',
    'USSR coop': '',
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
    'Manchukuo': '',
    'Siam': '',
    'Vichy': ''
}
reserv_template_pony = {
    'EQUESTRIA MAIN': '',
    'EQUESTRIA COOP': '',
    'CRYSTAL EMPIRE': '',
    'NEW MARELAND': '',
    'STALLIONGRAD': '',
    'CHANGELING LANDS MAIN': '',
    'CHANGELING LANDS COOP': '',
    'CHANGELING LANDS COOP #2': '',
    'OLENIA': '',
    'POLAR BEARS': '',
    'WINGBARDY': '',
    'HIPPOGRIFFIA MAIN': '',
    'HIPPOGRIFFIA COOP': '',
    'COLTHAGE': '',
    'CHIROPTERRA': '',
    'BUFFALO KINGDOM': '',
    'WARZENA KINGDOM': ''
}

def update_quotes(quote: str):
    """Update quotes list in DB with a new quote

    Args:
        quote (str): quote from player
    """
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
    """Deletes last adde quote from DB

    Raises:
        EmptyError: there is no quotes
    """
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        base = base[:-1]
        db.update({'content': base}, Cursor.name == "player_quotes")
        return
    else:
        raise EmptyError


def delete_quote(index: int):
    """Deletes quote by index

    Args:
        index (int): index of quote

    Raises:
        EmptyError: there is no quotes
    """
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
    """Gets random quote from DB

    Raises:
        EmptyError: there is no quotes

    Returns:
        str: random_quote
    """
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        random_quote = random.choice(base)
        return random_quote
    else:
        raise EmptyError


def get_list():
    """Gets list of quotes from DB

    Raises:
        EmptyError:  there is no quotes

    Returns:
        str: one string made from list
    """
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
    """Gets last adde quote

    Raises:
        EmptyError: there is no quotes

    Returns:
        str:  last_quote
    """
    dict_quotes = db.get(Cursor.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        last_quote = base[-1]
        return last_quote
    else:
        raise EmptyError


def open_res():
    """Opens reservations and allows to write in DB also clean DB before that
    """
    if db.get(Cursor.name == "reservations"):
        db.update({'content': reserv_template, 'flag': True},
                  Cursor.name == "reservations")
    else:
        db.insert({'name': 'reservations',
                   'content': reserv_template, 'flag': True})

def open_res_pony():
    if db.get(Cursor.name == "reservations_pony"):
        db.update({'content': reserv_template_pony, 'flag': True},
                  Cursor.name == "reservations_pony")
    else:
        db.insert({'name': 'reservations_pony',
                   'content': reserv_template_pony, 'flag': True})

def update_res(user: str, country: str):
    """Add reserv from a user into DB

    Args:
        user (str): user
        country (str): reserverd nation
    """
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        base[country] = user
        db.update({'content': base}, Cursor.name == "reservations")
    else:
        db.insert({'name': 'reservations', 'content': {country: user}})

def update_res_pony(user, country):
    if db.get(Cursor.name == "reservations_pony"):
        dict_reservations = db.get(Cursor.name == "reservations_pony")
        base = dict_reservations['content']
        base[country] = user
        db.update({'content': base}, Cursor.name == "reservations_pony")
    else:
        db.insert({'name': 'reservations_pony', 'content': {country: user}})

def remove_res(user):
    """Deletes reservation made by user

    Args:
        user (str): user
    """
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        for key, value in base.items():
            if user == value:
                base[key] = ''

        db.update({'content': base}, Cursor.name == "reservations")

def remove_res_pony(user):
    if db.get(Cursor.name == "reservations_pony"):
        dict_reservations = db.get(Cursor.name == "reservations_pony")
        base = dict_reservations['content']
        for key, value in base.items():
            if user == value:
                base[key] = ''

        db.update({'content': base}, Cursor.name == "reservations_pony")

def get_res() -> dict|int:
    """Gets current reservations and total number of players

    Returns:
        dict: reservations
        int: total number of players
    """
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        count = 0
        for key, value in base.items():
            if value != '':
                count += 1
        return base, count

def get_res_pony():
    if db.get(Cursor.name == "reservations_pony"):
        dict_reservations = db.get(Cursor.name == "reservations_pony")
        base = dict_reservations['content']
        count = 0
        for key, value in base.items():
            if value != '':
                count += 1
        return base, count

def close_res():
    """Closes res, cleans DB
    """
    if db.get(Cursor.name == "reservations"):
        db.update({'content': reserv_template, 'flag': False},
                  Cursor.name == "reservations")
    else:
        db.insert({'name': 'reservations',
                   'content': reserv_template, 'flag': False})

def close_res_pony():
    if db.get(Cursor.name == "reservations_pony"):
        db.update({'content': reserv_template_pony, 'flag': False},
                  Cursor.name == "reservations_pony")
    else:
        db.insert({'name': 'reservations_pony',
                   'content': reserv_template_pony, 'flag': False})

def get_flag() -> bool:
    """Gets flag is reservations are open or not

    Returns:
        flag(bool): are res open or not
    """
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        flag = dict_reservations['flag']
        return flag

def get_flag_pony():
    if db.get(Cursor.name == "reservations_pony"):
        dict_reservations = db.get(Cursor.name == "reservations_pony")
        base = dict_reservations['flag']
        return base

def get_country_by_user(user: str) -> str:
    """Gets nation by user

    Args:
        user (str): user 

    Returns:
        str: reserved nation
    """
    if db.get(Cursor.name == "reservations"):
        dict_reservations = db.get(Cursor.name == "reservations")
        base = dict_reservations['content']
        for key, value in base.items():
            if user == value:
                return str(key)
            
def get_country_by_user_pony(user):
    if db.get(Cursor.name == "reservations_pony"):
        dict_reservations = db.get(Cursor.name == "reservations_pony")
        base = dict_reservations['content']
        for key, value in base.items():
            if user == value:
                return str(key)