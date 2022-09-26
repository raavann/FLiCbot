import discord
bot = discord.Bot()

from commands.verify import Verify
@bot.slash_command()
async def verify(ctx: discord.ApplicationContext):
    # modal = Verify(title="Verify yourself")
    # await ctx.send_modal(modal)
    if(ctx.channel_id == 1021877729446068345):
        modal = Verify(title="Verify yourself")
        await ctx.send_modal(modal)
    else:
        await ctx.response.send_message("You can not use this command, contact admins if you think this is a mistake!", ephemeral=True)

from db import find
@bot.slash_command()
async def info(
    ctx: discord.ApplicationContext, 
    whatyouknow: discord.Option(str, required=True,choices=["name", "discordId", "email", "_id"], description="Select what you know..."),
    value: discord.Option(str, required=True, description="Value to find")
):
    await ctx.response.defer()
    member = await find({str(whatyouknow):str(value)})
    if(member):
        await ctx.respond(embed=discord.Embed(title="Information", color=discord.Color.green(), description="Information of users")
        .add_field(name= "Name", value=member["name"], inline=False)
        .add_field(name="Email", value=member['email'], inline=False)
        .add_field(name="Branch", value=member['branch'], inline=False)
        .add_field(name="Batch", value=member['batch'], inline=False)
        .add_field(name="Discord Username", value=ctx.guild.get_member(int(member['discordId'])) ) ,delete_after=15)
    else:
        await ctx.respond("No user found with this information", delete_after=15)

@bot.slash_command()
async def infoall(
    ctx: discord.ApplicationContext, 
    whatyouknow: discord.Option(str, required=True,choices=["name", "discordId", "email", "_id"], description="Select what you know..."),
    value: discord.Option(str, required=True, description="Value to find")
):
    await ctx.response.defer()

    whatyouknow = whatyouknow.strip()
    value = value.strip()
    newset = False
    msg = ''
    for role in ctx.user.roles:
        if(str(role.id) == '1015228310583791636' or str(role.id) == '1015226281941536879'):
            newset = True
            break

    if(newset == False):
        msg =  f"Sorry you can not access this command! Only Heads and Admins can!"
    else:
        member = await find({str(whatyouknow):str(value)})
        msg = f"{str(member)}"
    
    await ctx.respond(msg, delete_after=15)

from dotenv import load_dotenv
import os
load_dotenv()
bot.run(os.getenv('TOKEN'))