from tinydb import TinyDB, Query
import random
import json

db = TinyDB('db.json')

User = Query()


class EmptyError(BaseException):
    def __init__(self):
        pass


# class PlayerQuotes:
#
#     def __init__(self, quotes_list):
#         self.quotes_list = quotes_list
#
#     def get_quotes_list(self):
#         return self.quotes_list
#
#     def get_num_list(self):
#         if self.quotes_list:
#             result_string = ''
#             for index, q in enumerate(self.quotes_list, 1):
#                 result_string = result_string + f"{index}. {q}\n"
#             return result_string
#
#     def get_random_quote(self):
#         if self.quotes_list:
#             return random.choice(self.quotes_list)
#
#     def add_quote(self, quote):
#         self.quotes_list.append(quote)
#
#     def delete_last(self):
#         if self.quotes_list:
#             self.quotes_list = self.quotes_list[:-1]
#
#     def delete_quote_by_index(self, index):
#         if self.quotes_list:
#             if len(self.quotes_list) >= index - 1:
#                 index_element = self.quotes_list.pop(index - 1)


def update_quotes(quote):
    if db.get(User.name == "player_quotes"):
        dict_quotes = db.get(User.name == "player_quotes")
        print(dict_quotes)
        base = dict_quotes['content']
        base.append(quote)
        print(base)
        db.update({'content': base})
    else:
        db.insert({'name': 'player_quotes', 'content': [quote]})


def delete_last_quote():
    dict_quotes = db.get(User.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        base = base[:-1]
        db.update({'content': base})
        return
    else:
        raise EmptyError


def delete_quote(index):
    dict_quotes = db.get(User.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        if len(base) >= index - 1:
            index_element = base.pop(index - 1)
            db.update({'content': base})
        return
    else:
        raise EmptyError


def get_random_quote():
    dict_quotes = db.get(User.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        random_quote = random.choice(base)
        print(random_quote)
        return random_quote
    else:
        raise EmptyError


def get_list():
    dict_quotes = db.get(User.name == "player_quotes")
    print(dict_quotes)
    base = dict_quotes['content']
    if type(base) is list:
        print(base)
        result_string = ''
        for index, q in enumerate(base, 1):
            result_string = result_string + f"{index}. {q}\n"
        return result_string
    else:
        raise EmptyError


def get_last():
    dict_quotes = db.get(User.name == "player_quotes")
    base = dict_quotes['content']
    if type(base) is list:
        last_quote = base[-1]
        return last_quote
    else:
        raise EmptyError


