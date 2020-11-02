import discord
import os
from discord.ext import commands
from random import *

bot= commands.Bot(command_prefix="$", description=":tools:")

def rock_paper(p_1,p_2):
    rock=2
    paper=3
    scissors=4
    roll_1=randint(2,4)
    roll_2=randint(2,4)
    if roll_1==2 and roll_2==2:
        result=":rock: Egalité :rock:"
    elif roll_1==3 and roll_2==3:
        result=":roll_of_paper: Egalité :roll_of_paper:"
    elif roll_1==4 and roll_2==4:
        result=":scissors: Egalité :scissors:"
    elif roll_1==4 and roll_2==3:
        result=f"{p_1} a gagné :scissors: :crossed_swords: :roll_of_paper:"
    elif roll_1==2 and roll_2==3:
        result= f"{p_2} a gagné :roll_of_paper: :crossed_swords: :rock:"
    elif roll_1==2 and roll_2==4:
        result= f"{p_1} a gagné :rock: :crossed_swords: :scissors:"
    elif roll_2==2 and roll_1==3:
        result= f"{p_1} a gagné :roll_of_paper: :crossed_swords: :rock:"
    elif roll_2==2 and roll_1==4:
        result= f"{p_2} a gagné :rock: :crossed_swords: :scissors:"
    elif roll_2==4 and roll_1==3:
        result=f"{p_2} a gagné :scissors: :crossed_swords: :roll_of_paper:"

    return result


@bot.event
async def on_ready():
    print("Bot Ready")

@bot.command()
async def dice(ctx):
    await ctx.send(f"Dé : {randint(1,6)}")

@bot.command()
async def opgg(ctx, name):
    summ_name=name.replace(" ","")
    await ctx.send(f"https://euw.op.gg/summoner/userName={summ_name.lower()}")

@bot.command()
async def duel(ctx,p_1,p_2):
    aff=rock_paper(str(p_1),str(p_2))
    await ctx.send(aff)



bot.run(os.environ['DISCORD_TOKEN'])