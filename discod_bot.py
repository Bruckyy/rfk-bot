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

@bot.command()
async def champion(ctx):
    champion=["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Ashe","Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Cassiopeia","Cho'Gath","Corki","Darius","Diana","Dr. Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Irelia","Janna","Jarvan IV","Jax","Jayce","Jinx","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kennen","Kha'Zix","Kindred","Kog'Maw","LeBlanc","Lee Sin","Leona","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Nidalee","Nocturne","Nunu","Olaf","Orianna","Pantheon","Poppy","Quinn","Rammus","Rek'Sai","Renekton","Rengar","Riven","Rumble","Ryze","Samira","Sejuani","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Syndra","Tahm Kench","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel'Koz","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong","Xerath","Xin Zhao","Yasuo","Yone","Yorick","Zac","Zed","Ziggs","Zilean","Zyra","Yuumi","Seraphine","Lillia","Sett","Aphelios","Senna","Qiyana","Sylas","Neeko","Pyke","Kai'Sa","Zoe","Ornn","Kayn","Rakan","Xayah","Camille","Ivern","Kled","Taliyah","Aurelion Sol","Jhin","Illaoi"]
    index=randint(1,151)-1
    aff=champion[index]
    await ctx.send(aff)


bot.run(os.environ['DISCORD_TOKEN'])