import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

start_components = [
    [Button(label='USA main', style=3, custom_id='usa_main'),
     Button(label='USA coop', style=3, custom_id='usa_coop'),
     Button(label='Germany main', style=3, custom_id='ger_main'),
     Button(label='Germany coop', style=3, custom_id='ger_coop'),
     Button(label='UK', style=3, custom_id='uk')]
]


def change_components(comp, reserves):
    pass