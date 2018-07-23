import random
from discord.ext.commands import Bot
from discord import Game
from discord.voice_client import VoiceClient
from discord.ext import commands
import requests
import asyncio
import time
from discord.voice_client import VoiceClient
from riotwatcher import RiotWatcher
from datetime import datetime 

#implement chatterbot?!?
#BOT_PREFIX = ("!")
TOKEN = "___" #token not inserted

startup_extensions = ["Music", "LeagueOfLegends"]

#client = Bot(command_prefix=BOT_PREFIX)
bot = commands.Bot("!")

########## leaguestuff ##############
watcher = RiotWatcher('___') #RiotWatcher is a constructor in the library, api key not inserted 

my_region = 'na1'

############ global variables #################################
trigger1 = True #for listservers(), stoplistingservers()
array1 = [] #for timer
isrunning1 = False #for timer
startup_time = 0 #for uptime, called in on_ready()


#######################   MUSIC STUFF   ########################################
class Main_Commands():
    def __init__(self, bot):
        self.bot=bot
        
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}: {}" .format(type(e).__name__, e)
            print("Failed to load extension {}\n{}" .format(extension, exc))
 
#######################   FUNCTIONS   ####################################
#while bots running, always spam when its a certain time in the general channel
async def my_background_task_timer():
    await bot.wait_until_ready()
    channel = bot.get_channel('309800853772959745')
    print(channel)
    while not bot.is_closed:
        global array1
        
        print(channel.name)
        
        trigger = False

        if channel not in array1:
            array1.append(channel)
            isrunning1 = False

        else:
            isrunning1 = True

        if not (isrunning1): 

            while True:
                isrunning1 = True
                current_time = time.localtime()
                string_time = time.strftime("%H, %M, %S", current_time)
                string_time = string_time.split(",")
                hour = int(string_time[0])
                minute = int(string_time[1])
                second = int(string_time[2])
                
                #print(hour-4, ":", minute, ":", second)
                print(hour, ":", minute, ":", second)
                        
                await asyncio.sleep(5)

                if trigger:
                    array1.remove(channel)
                    break;

                while ((hour==4) and (minute==20)) or ((hour==16) and (minute==20)):
                    current_time = time.localtime()
                    string_time = time.strftime("%H, %M, %S", current_time)
                    string_time = string_time.split(",")
                    hour = int(string_time[0])
                    minute = int(string_time[1])
                    second = int(string_time[2])

                    #print(hour-4, ":", minute, ":", second)
                    print(hour, ":", minute, ":", second)
                            
                    await asyncio.sleep(5)
                    
                    print("trigger is trig'd")
                    trigger = True
                    for i in range(3):
                        await bot.send_message(bot.get_channel('309800853772959745'), 'SPAM')
#ml
@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="ml simulator 2018"))
    print("Logged in as " + bot.user.name)
    bot.loop.create_task(my_background_task_timer())
    global startup_time
    list_time = time.localtime()
    string_time = time.strftime("%d,%H, %M, %S", list_time)
    startup_time = string_time
    startup_time = startup_time.split(",")
    await bot.send_message(bot.get_channel('309800853772959745'), "startup message")

 #   default_channels = []
 #   for server in bot.servers:
 #       try:
 #           default_channels += [[server.id, server.default_channel.name]]
 #       except Exception:
 #           print("server \"", server, "\" does not have a default channel")
 #   print(default_channels)
 #   for i in default_channels:
 #       fourtwen_call(i[0])
       
    
#uptime
@bot.command(description="Prints the uptime of the bot.", brief="Uptime of the bot.", aliases=("uptime", "upt"))
async def up_time():
    #handling startup time
    global startup_time
    print(startup_time)
    string_time_startup = startup_time[0].strip() + ":" + startup_time[1].strip() + ":" + startup_time[2].strip() + ":" + startup_time[3].strip()
    print(string_time_startup)
    #format for time
    FMT = '%d:%H:%M:%S'
    
    #handling local time
    list_time = time.localtime()
    string_time = time.strftime("%d,%H, %M, %S", list_time)
    current_time = string_time
    current_time = current_time.split(",")
    print(current_time)
    string_time_current = current_time[0].strip() + ":" + current_time[1].strip() + ":" + current_time[2].strip() + ":" + current_time[3].strip()
    print(string_time_current)

    #time difference calculations
    tdelta = datetime.strptime(string_time_current, FMT) - datetime.strptime(string_time_startup, FMT)
    print(tdelta)
    await bot.say("Current uptime: %s" %tdelta)
    
    
@bot.command(name="fourtwenball", description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=("eight_ball", "eightball", "8-ball", "420ball"),
                pass_context=True)               
async def eight_ball(context):
    possible_responses = [
        "Could be",
        "Might be",
        "Prolly is",
        "Confirmed",
        "Too hard to tell",
        "That is definitely not the case",
        "With absolute certainty"
        ]

    await bot.say(random.choice(possible_responses)+ ", young " + context.message.author.mention)

#toxx
@bot.command(description="Mentions toxic120.", brief="@Toxx", aliases=("toxic420", "toxic120", "2197", "cody", "toxic", "zollis", "toxl", "voxl", "vollis", "twitchextension110characters"))
async def toxx():
    toxxid = "<@124320398383906817>"
    await bot.say("%s" %toxxid)

#men
@bot.command(description="Mentions slick haus.", brief="@Slickhaus", aliases=("slickmoss", "moss", "men", "ment", "menshlog", "menshlig", "mentog", "mennis", "slickety", "slockney", "slick noss", "slick"))
async def slickhaus():
    menid = "<@251514815275728896>"
    await bot.say("%s" %menid)
    
#leaguenerds
@bot.command(description="Mentions the league nerds.", brief="@Leaguenerds", aliases=("leaguenerds", "leaguefam", "league", "lolnerds"))
async def league_nerds():
    toxxid = "<@124320398383906817>"
    await bot.say("%s" %toxxid)
    klyid = "<@220073855576702977>"
    await bot.say("%s" %klyid)
    jaseid = "<@124319194735968259>"
    await bot.say("%s" %jaseid)
    restinpiecesid = "<@258705909021278209>"
    await bot.say("%s" %restinpiecesid)
    xzeroid = "<@166325720073764865>"
    await bot.say("%s" %xzeroid)
    quingeid = "<@222903183285026826>"
    await bot.say("%s" %quingeid)
    rockid = "<@297045144559943680>"
    await bot.say("%s" %rockid)
    menid = "<@251514815275728896>"
    await bot.say("%s" %menid)

#wownerds
@bot.command(description="Mentions the wow nerds.", brief="@Wownerds", aliases=("wownerds", "wowfam", "wow", "vanillnerds", "vanill"))
async def wow_nerds():
    toxxid = "<@124320398383906817>"
    await bot.say("%s" %toxxid)
    klyid = "<@220073855576702977>"
    await bot.say("%s" %klyid)
    jaseid = "<@124319194735968259>"
    await bot.say("%s" %jaseid)
    restinpiecesid = "<@258705909021278209>"
    await bot.say("%s" %restinpiecesid)
    reqid = "<@267807400315191297>"
    await bot.say("%s" %reqid)
    codyid = "<@119858392343773184>"
    await bot.say("%s" %codyid)
    menid = "<@251514815275728896>"
    await bot.say("%s" %menid)
   

#quanjaswanjas
@bot.command(description="Mentions quanjaswanjas.", brief="@Quanjaswanjas", aliases=("lilwanajs", "wanjas", "quanjaslittlewanjas", "quanjaswanjas"))
async def summonwanjas():
    tucanid = "<@223242063016099851>"
    await bot.say("%s" %tucanid)
    klyid = "<@220073855576702977>"
    await bot.say("%s" %klyid)
    giraardid = "<@188520370364481536>"
    await bot.say("%s" %giraardid)
    quingeid = "<@222903183285026826>"
    await bot.say("%s" %quingeid)
    unkwid = "<@441394580206649344>"
    await bot.say("%s" %unkwid)
    poutineid = "<@71931177589551104>"
    await bot.say("%s" %poutineid)

#quanjaswanjas
@bot.command(description="Mentions 2can not quanja.", brief="@2can not quanjas", aliases=("200iqshotcaller", "200iq", "shotcaller"))
async def teamleader():
    tucanid = "<@223242063016099851>"
    await bot.say("%s" %tucanid)
 
#req
@bot.command(description="Mentions officer reqtko.", brief="@Req", aliases=("requel", "reqtko", "requiem", "reqiuem"))
async def req():
    reqid = "<@267807400315191297>"
    await bot.say("%s" %reqid)

#rock
@bot.command(description="Mentions rockette.", brief="@Rock(ette)", aliases=("rockette", "rockquel", "joe"))
async def rock():
    rockid = "<@297045144559943680>"
    await bot.say("%s" %rockid)

#sap
@bot.command(description="Mentions YUNG SAP.", brief="@Sapler", aliases=("sapler", "garex", "sapler/garex", "sapless"))
async def sap():
    sapid = "<@177975679994953728>"
    await bot.say("%s" %sapid)

#kly
@bot.command(description="Mentions kly.", brief="@Kly", aliases=("kly9", "klynine"))
async def kly():
    klyid = "<@220073855576702977>"
    await bot.say("%s" %klyid)

#kai
@bot.command(description="Mentions restinpieces1397-iwnl69.", brief="@Restinpieces", aliases=("restinpieces", "ripinpeaces", "learntotannl", "rip", "kai", "conflictresolution"))
async def aetherflash():
    restinpiecesid = "<@258705909021278209>"
    await bot.say("%s" %restinpiecesid)

#jason
@bot.command(description="Mentions Jason1234500.", brief="@Jason1234500", aliases=("berje", "fatherml", "jeloss", "jolonquiy", "berjelesason", "berjase", "bjorn", "riot10", "riotten", "jay", "jaysmr", "jebreskeberjelason", "jebreskeberjelesason"))
async def jason():
    jaseid = "<@124319194735968259>"
    await bot.say("%s" %jaseid)

#cody
@bot.command(description="Mentions decodii69.", brief="@Decodii", aliases=("sode", "cole"))
async def code():
    codyid = "<@119858392343773184>"
    await bot.say("%s" %codyid)

#bitchcrank
@bot.command(description="Mentions xXxbitchcrankxXx.", brief="@Xzero", aliases=("zero", "small", "crank", "bitchcrank", "joey"))
async def xzero():
    xzeroid = "<@166325720073764865>"
    await bot.say("%s" %xzeroid)
    
#isaac
@bot.command(description="Mentions the one and only isaacborne.", brief="@Isaac", aliases=("borne", "isaacborne", "ize"))
async def isaac():
    isaacid = "<@143796959965216768>"
    await bot.say("%s" %isaacid)
    
#quinge
@bot.command(description="Mentions the notorious V I C.", brief="@Quinge", aliases=("quanj", "quanjawanja", "quingey", "quingeywingy", "winjy", "rankggod", "victor", "vic", "quanjaless", "wanja"))
async def quinge():
    quingeid = "<@222903183285026826>"
    await bot.say("%s" %quingeid)

#tom
@bot.command(description="Mentions the young tomothy.", brief="@Slimthicc",  aliases=("slim", "slimthicc", "englishraidlead", "mot", "obsuh", "obsuhleet", "obz", "obs"))
async def tom():
    tomid = "<@314942798610563072>"
    await bot.say("%s" %tomid)

#square a number
@bot.command(name="square", description="Squares a given number.", brief="Squares a number.", aliases=("sqr", "squarenumb"))
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is: " + str(squared_value))
    
#esea link
@bot.command(name="esea", description="Links the esea team page (ez main).", brief="Links the esea team page.", aliases=("eseateam", "5pnd", "5PND"))
async def esea_team():
    await bot.say("https://play.esea.net/teams/8719655")

@bot.command(name="listservers", description="Lists servers currently using ML bot (Updates every 10 seconds).", brief="Lists servers currently using ML bot.")
async def list_servers():
    await bot.wait_until_ready()
    global trigger1
    trigger1 = True
    while trigger1:
        print("current servers:")
        await bot.say("current servers:")
        for server in bot.servers:
            await bot.say(server.name)
            print(server.name)
        await asyncio.sleep(10)

@bot.command(name="stoplistingservers", description="Stops the function listservers.", brief="Stops the function listservers.")
async def stop_listing_servers():
    global trigger1
    trigger1 = False
    await bot.say("Stopping listservers")
        
@bot.command(name="roll", description="Two options: \n 1. Given no numbers as arguments , will roll by default 1-100. \n 2. Given a number y, randomly select a number between 1-y \n 3. Given two numbers in the format x-y, randomly select a number between x-y ", brief="Roll (1-y), (x-y).")
async def roll_number(args=''):
    sep_nums = args.split("-")

    #deal with arguments
    
    if len(sep_nums) == 1:
        if sep_nums[0]=='':
            num1 = 1
            num2 = 100
        else:
            num1 = 1
            num2 = int(sep_nums[0])

    elif len(sep_nums) ==2:
        num1 = int(sep_nums[0])
        num2 = int(sep_nums[1])

    else:
        await bot.say("That's some invalid gameplay.")

    #we have the arguments in the form of num1 and num2 now, we can do what we wanted to

    if num2<num1:
        await bot.say("number has to be more than %s dawg" %num1)

    elif num1==num2:
        await bot.say(num1)
        
    else:
        value = str(random.randint(num1,num2))
        print(value)
        await bot.say(value)
    
        

# Returns a link to a random cat picture or cat gif
@bot.command(name="catpic", description="Posts an ML cat pic.", brief="Posts a cat pic.")
async def getCatPicture():
    catPicture = requests.get('http://thecatapi.com/api/images/get.php')
    print(catPicture.status_code)
    if catPicture.status_code == 200:
        print(catPicture.url)
        await bot.say(catPicture.url)

    else:
        print('Error 404. Website may be down.')
        await bot.say('Error 404. Website may be down.')

# Returns a link to a random cat gif
@bot.command(name="catgif", description="Posts an ML cat gif.", brief="Posts a cat gif.")
async def getCatGif():
    catGif = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
    if catGif.status_code == 200:

        print(catGif.status_code)
        print(catGif.url)
        await bot.say(catGif.url)

    else:
        print('Error 404. Website may be down.')
        await bot.say('Error 404. Website may be down.')



#SPAM WHEN ITS A CERTAIN TIME
@bot.command(name="certaintime", description="Alerts users when it's a certain time." , brief="Alerts users when its a certain time.", pass_context=True)
async def spamtime(ctx):
    global array1
    
    print(ctx.message.channel.name)
    print(ctx.message.channel)
    
    trigger = False
    channel = str(ctx.message.channel.id)

    if channel not in array1:
        array1.append(channel)
        isrunning1 = False

    else:
        isrunning1 = True

    if not (isrunning1): 

        while True:
            isrunning1 = True
            current_time = time.localtime()
            string_time = time.strftime("%H, %M, %S", current_time)
            string_time = string_time.split(",")
            hour = int(string_time[0])
            minute = int(string_time[1])
            second = int(string_time[2])

            #print(hour-4, ":", minute, ":", second)
            print(hour, ":", minute, ":", second)
                    
            await asyncio.sleep(5)

            if trigger:
                array1.remove(channel)
                break;

            while ((hour==4) and (minute==20)) or ((hour==16) and (minute==20)):
                current_time = time.localtime()
                string_time = time.strftime("%H, %M, %S", current_time)
                string_time = string_time.split(",")
                hour = int(string_time[0])
                minute = int(string_time[1])
                second = int(string_time[2])

                #print(hour-4, ":", minute, ":", second)
                print(hour, ":", minute, ":", second)
                        
                await asyncio.sleep(5)
                
                print("trigger is trig'd")
                trigger = True
                for i in range(3):
                    await bot.say("SPAM")


@bot.command(name="blimpfacts", description="Informs the fam of a random blimp fact.",
                brief="Blimp facts for code.",
                aliases=("blimpfact", "blimps", "blimpy", "blimp"),
                pass_context=True)               
async def blimp_facts():
    possible_responses = [
        "The first airship was invented by Henri Giffard in 1852. He launched his ship from the Paris Hippodome, traveling about 20 miles at a speed of 6 miles per hour.",
        "The first airships contained hydrogen, which is lighter than air. Hydrogen is also very flammable and dangerous. It was replaced by helium.",
        "Ferninand, Count Von Zeppelin made highly successful airships in 1900. Germany used these ships during World War 1 to bomb London and France.",
        "In 1928, the Graf Zeppelin was completed. This airship made 590 flights and crossed the Atlantic Ocean 144 times.",
        "Passengers regularly traveled across the ocean in the Graf Zeppelin.",
        "Airship travel was discontinued in the late 1930s because the ships were expensive to operate and maintain. They were also dangerous and often crashed in storms.",
        "On May 6, 1937, The Hindenburg Zeppelin was landing in Lakehurst, New Jersey, after crossing the Atlantic Ocean. Just moments before landing, the ship erupted in flames and was engulfed in less than one minute. 62 of the 97 people aboard miraculously survived. Most of them jumped from the windows of the airship. This disaster marked the end of commercial travel by airships.",
        "Blimps are in the category of LTA vehicles, which stands for lighter than air.",
        "Blimps are filled with helium, an inert gas.",
        "There are more astronauts in the world than blimp pilots.",
        "Blimps date back to the mid-1800s.",
        "You can fit 75 million golf balls in a blimp.",
        "Blimps lift due to high pressure and helium pumped in the balloon.",
        "A blimp uses less fuel in two weeks than it takes a 747 airplane just to taxi to the runway.",
        "The only solid parts of a blimp are the gondola, where the passengers are, and the tail fins used for stability.",
        "Blimps require propeller motors for steering mobility purposes.",
        "Some blimps were used for patrolling purposes for the United States Navy in the World War I period.",
        "Blimps belong to a family of aircrafts called \"airships,\" defined as an aircraft that doesn’t use wings to fly.",
        "A blimp is an airship that has no internal framework to keep its helium gas bag rigid.",
        "Pilots power and steer blimps with two propeller engines and a movable tail and rudder system.",
        "Cody Wilson, a moderately young quake player living in Sarnia (Canada) is known in the international blimp community as one of the biggest blimp enthusiasts in the Northern Hemisphere.",
        "On average, blimps can travel 150-200 miles per day.",
        "There are 4 air valves on each blimp- two at the front and two at the back. The valves are opened and closed to either let air out or keep air in the ballonets.",
        "The usual cruising speed for a blimp is 35 miles per hour in a zero wind condition.",
        "Airships can carry enough fuel to fly for twenty-four hours, although they rarely do.",
        "Without any lifting gas, the empty ship (GZ-20) weighs about 12,840 pounds. Inflated with helium, the ship weighs only 100-200 pounds, depending on the amount of fuel, payload and ballast aboard.",
        "Unlike semi-rigid and rigid airships (e.g. Zeppelins), blimps rely on the pressure of the lifting gas (usually helium, rather than hydrogen) inside the envelope and the strength of the envelope itself to maintain their shape.",
        "Since blimps keep their shape with internal overpressure, typically the only solid parts are the passenger car (gondola) and the tail fins.",
        "The fastest a blimp can fly is 53 miles per hour.",
        "The 1964 James Bond film, Goldfinger, featured a Goodyear Blimp in the opening titles.",
        "A CBS producer paid $1000 to use the Goodyear blimp to televise the 1960 Orange Bowl football game in Miami, Florida.",
        "Blimps are made of polyester and rubber",
        "The idea of a blimp first came from a hot air balloon."
        ]

    await bot.say(random.choice(possible_responses))



#client.run(TOKEN)
bot.run(TOKEN)
