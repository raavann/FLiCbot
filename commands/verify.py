from random import Random
import discord
from db import find ,update
from datetime import datetime

import logging
logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.WARNING,)

class Verify(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Email", placeholder="Enter your email", required=True))
        self.add_item(discord.ui.InputText(label="Pass Code", style=discord.InputTextStyle.short, placeholder="Enter your pass code", required=True))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        member = await find({"email": self.children[0].value})
        # print( datetime.now() ,member)
        logging.warning(datetime.now(), member)

        isequal = False
        if (member != None and type(member)==dict and str(member['passCode']) == str(self.children[1].value)):
            isequal = True
            await interaction.user.send(f"{interaction.user} has been verified!")
        else:
            await interaction.user.send(f"{interaction.user } Invalid email or pass code")

        if(isequal):
            await interaction.user.add_roles(interaction.guild.get_role(1015227226406522923))
            await interaction.user.remove_roles(interaction.guild.get_role(1021877916579143872))
            rand = Random().randint(10000, 999999)
            await update(
                {"email":self.children[0].value},
                {"$set":{
                    "passCode": rand, 
                    "discordId":str(interaction.user.id)
                    }
                }
            )
