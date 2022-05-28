import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

start_components = [
    Button(label='USA', style=3, custom_id='usa_button'),
    Button(label='Germany', style=3, custom_id='ger_button'),
    Button(label='UK', style=3, custom_id='uk_button')
]


def change_components(comp, reserves):
    pass