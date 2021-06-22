import discord
import asyncio
import os
import wikipedia
from discord.ext import commands
from random import randint
from time import sleep
from riotwatcher import LolWatcher, ApiError


bot= commands.Bot(command_prefix="$", description=":tools:")

def rock_paper(p_1,p_2):
    roll=randint(1,2)
    if roll==1:
        result=f"{p_1} a Gagné !"
    else:
        result=f"{p_2} a Gagné !"
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
    champion=["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Ashe","Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Cassiopeia","Cho'Gath","Corki","Darius","Diana","Dr. Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Irelia","Janna","Jarvan IV","Jax","Jayce","Jinx","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kennen","Kha'Zix","Kindred","Kog'Maw","LeBlanc","Lee Sin","Leona","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Nidalee","Nocturne","Nunu","Olaf","Orianna","Pantheon","Poppy","Quinn","Rammus","Rek'Sai","Renekton","Rengar","Riven","Rumble","Ryze","Samira","Sejuani","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Syndra","Tahm Kench","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel'Koz","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong","Xerath","Xin Zhao","Yasuo","Yone","Yorick","Zac","Zed","Ziggs","Zilean","Zyra","Yuumi","Seraphine","Lillia","Sett","Aphelios","Senna","Qiyana","Sylas","Neeko","Pyke","Kai'Sa","Zoe","Ornn","Kayn","Rakan","Xayah","Camille","Ivern","Kled","Taliyah","Aurelion Sol","Jhin","Illaoi","Rell","Viego","Gwen"]
    index=randint(0,len(champion)-1)
    aff=champion[index]
    await ctx.send(aff)

@bot.command()
async def role(ctx,role):
with open('champ.json') as json_file:
        champ = json.load(json_file)
    rand=randint(0,len(champ[role])-1)
    liste=(list(champ[role]))
    await ctx.send(liste[rand])

@bot.command()
async def summoner(ctx,name,region):
    """
    region: BR1/EUN1/EUW1/JP1/KR/LA1/LA2/NA1/OC1/TR1/RU
    """
    api_key = os.environ['RIOT_TOKEN']
    watcher = LolWatcher(api_key)
    me = watcher.summoner.by_name(region,name)
    my_ranked_stats = watcher.league.by_summoner(region,me['id'])
    i=0
    z=0
    while i<len(my_ranked_stats):
        val=list(my_ranked_stats[i].values())
        j=0
        while j<len(my_ranked_stats[i]):
            if val[j]=='RANKED_SOLO_5x5':
                z=i
            j+=1

        i+=1

    solo = my_ranked_stats[z]
    winrate = round(solo["wins"]/(solo["wins"]+solo["losses"])*100)
    tier=solo["tier"]
    rank=solo["rank"]
    wins=solo["wins"]
    losses=solo["losses"]
    nom=solo["summonerName"]
    lp=solo["leaguePoints"]
    aff="Rank: " + tier +" " + rank + " LP: "+ str(lp) + " Winrate: " + str(winrate)+"%"+ " W: " + str(wins) + " L: " + str(losses)
    aff2="SOLO RANKED informations for " + nom 
    await ctx.send(aff2)
    await ctx.send(aff)

@bot.command()
async def wiki(ctx,sub):
    """
    Affiche la page wikipedia passé en paramétre
    """
    try:
        wikipedia.set_lang("fr")
        result= wikipedia.page(sub)
        await ctx.send(result.summary)
    except:
        await ctx.send("Page: "+sub+" Introuvable")

bot.run(os.environ['DISCORD_TOKEN'])
