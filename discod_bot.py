import discord
import asyncio
import os
from discord.ext import commands
from random import randint
from selenium import webdriver
from time import sleep
from riotwatcher import LolWatcher, ApiError

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)



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
    champion=["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Ashe","Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Cassiopeia","Cho'Gath","Corki","Darius","Diana","Dr. Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Irelia","Janna","Jarvan IV","Jax","Jayce","Jinx","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kennen","Kha'Zix","Kindred","Kog'Maw","LeBlanc","Lee Sin","Leona","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Nidalee","Nocturne","Nunu","Olaf","Orianna","Pantheon","Poppy","Quinn","Rammus","Rek'Sai","Renekton","Rengar","Riven","Rumble","Ryze","Samira","Sejuani","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Syndra","Tahm Kench","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel'Koz","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong","Xerath","Xin Zhao","Yasuo","Yone","Yorick","Zac","Zed","Ziggs","Zilean","Zyra","Yuumi","Seraphine","Lillia","Sett","Aphelios","Senna","Qiyana","Sylas","Neeko","Pyke","Kai'Sa","Zoe","Ornn","Kayn","Rakan","Xayah","Camille","Ivern","Kled","Taliyah","Aurelion Sol","Jhin","Illaoi","Rell","Viego"]
    index=randint(1,len(champion))-1
    aff=champion[index]
    await ctx.send(aff)

@bot.command()
async def role(ctx,role):
    dico_roles={"top":["Aatrox","Akali","Cho'Gath","Darius","Dr.Mundo","Fiora","Gangplank","Garen","Illaoi","Irelia","Jax","Jayce","Kayle","Kennen","Kled","Lucian","Malphite","Maokai","Mordekaiser","Nasus","Poppy","Quinn","Renekton","Riven","Rumble","Sett","Shen","Singed","Sion","Sylas","Tahm Kench","Teemo","Tryndamere","Urgot","Vayne","Vladimir","Volibear","Wukong","Yasuo","Yone","Yorick","Ornn","Gnar","Camille"],
                "jungle":["Amumu","Ekko","Elise","Evelynn","Fiddlesticks","Gragas","Graves","Hecarim","Yvern","Jarvan IV","Jax","Karthus","Kayn","Kha'Zix","Kindred","Lee Sin","Lillia","Maître Yi","Nidalee","Nocturne","Nunu et Willump","Olaf","Rammus","Rek'Sai","Rengar","Sejuani","Sett","Shaco","Shyvana","Skarner","Sylas","Taliyah","Trundle","Udyr","Vi","Volibear","Warwick","Xin Zhao","Zac","Viego"],
                "mid":["Ahri","Akali","Anivia","Annie","Aurelion Sol","Azir","Cassiopeia","Corki","Diana","Ekko","Fizz","Galio","Heimerdinger","Irelia","Kassadin","Katarina","Leblanc","Lissandra","Lucian","Lux","Malzahar","Neeko","Orianna","Qiyana","Ryze","Seraphine","Sylas","Syndra","Talon","Twisted Fate","Veigar","Viktor","Vladimir","Xerath","Yasuo","Yone","Zed","Ziggs","Zoé","Gwen"],
                "adc":["Aphelios","Ashe","Caitlyn","Draven","Ezreal","Jhin","Jinx","Kai'Sa","Kalista","Kog'Maw","Lucian","Miss Fortune","Samira","Senna","Sivir","Tristana","Twitch","Varus","Xayah","Yasuo"],
                "supp":["Alistar","Bard","Blitzcrank","Brand","Braum","Janna","Karma","Leona","Lulu","Lux","Malphite","Maokai","Morgana","Nami","Nautilus","Pantheon","Pyke","Rakan","Senna","Seraphine","Sett","Sona","Soraka","Swain","Tahm Kench","Taric","Thresh","Vel'koz","Xerath","Yuumi","Zilean","Zyra","Rell"]
    }
    rand=randint(1,len(dico_roles[role]))
    liste=(list(dico_roles[role]))
    aff=liste[rand]
    await ctx.send(aff)

@bot.command()
async def summoner(ctx,name,region):
    api_key = os.environ['RIOT_TOKEN']
    region = region+'1'
    watcher = LolWatcher(api_key)
    me = watcher.summoner.by_name(region,name)
    my_ranked_stats = watcher.league.by_summoner(region,me['id'])
    solo = my_ranked_stats[1]
    winrate = round(solo["wins"]/(solo["wins"]+solo["losses"])*100)
    aff="Rank : " + solo["tier"] + " " + solo["rank"] + " LP : "+ solo["leaguePoints"] +" Winrate : " +  winrate+ "%" + " Wins : "+solo["wins"] + " Losses : " + solo["losses"]
    await ctx.send(aff)

bot.run(os.environ['DISCORD_TOKEN'])
