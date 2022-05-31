import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

start_components = [
    [Button(label='UK', style=3, custom_id='uk'),
     #Button(label='USA main', style=3, custom_id='usa_main'),
     #Button(label='USA coop', style=3, custom_id='usa_coop'),
     #Button(label='France', style=3, custom_id='france'),
     #Button(label='USSR main', style=3, custom_id='ussr_main'),
     #Button(label='USSR coop', style=3, custom_id='ussr_coop'),
     #Button(label='Mongolia', style=3, custom_id='mongolia')],
    
     #[Button(label='China', style=3, custom_id='china'),
     #Button(label='British Raj', style=3, custom_id='british_raj'),
     #Button(label='Canada', style=3, custom_id='canada'),
     #Button(label='Australia', style=3, custom_id='australia'),
     #Button(label='South Africa', style=3, custom_id='south_africa')],
     
     #[Button(label='New Zealand', style=3, custom_id='new_zealand'),
     #Button(label='Mexico', style=3, custom_id='mexico'),
     #Button(label='Brazil', style=3, custom_id='brazil')],
     
     #[Button(label='Germany main', style=3, custom_id='ger_main'),
     #Button(label='Germany coop', style=3, custom_id='ger_coop'),
     #Button(label='Italy', style=3, custom_id='italy'),
     #Button(label='Japan main', style=3, custom_id='japan_main'),
     #Button(label='Japan coop', style=3, custom_id='japan_coop')],
     
     #[Button(label='Hungary', style=3, custom_id='hungary'),
     #Button(label='Romania', style=3, custom_id='romania'),
     #Button(label='Bulgaria', style=3, custom_id='bulgaria'),
     #Button(label='Spain', style=3, custom_id='spain'),
     #Button(label='Finland', style=3, custom_id='finland'),
     #Button(label='Vichy France', style=3, custom_id='vichy'),
     #Button(label='Manchukuo', style=3, custom_id='manchukuo'),
     #Button(label='Siam', style=3, custom_id='siam')]
]]


def change_components(comp, reservations):
    
    for key, value in reservations.items():
        if value != '':
            for main_list in comp:
                for item in main_list:
                    if str(item.label) == key:
                        item.style = 2
    return comp

def check_reservations(interaction, reserves):
    button_clicked = str(interaction.component.label)
    print(button_clicked)
    author_clicked = str(interaction.author)
    print(author_clicked)
    for key, value in reserves.items():
        print(key, value)
        if value == author_clicked or (key == button_clicked and value != ''):
            return False

            
    return True